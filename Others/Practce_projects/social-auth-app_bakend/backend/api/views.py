# backend/api/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# FIX: Correct import for generating random strings/passwords in modern Django
# Replaced 'make_random_password' which was removed in Django 3.1+
from django.utils.crypto import get_random_string

# For Google ID token verification
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from google.auth import exceptions as google_auth_exceptions

# allauth imports for social login
from allauth.socialaccount.models import SocialAccount
# GoogleProvider is not strictly used in this view's logic, but fine to keep if needed elsewhere
from allauth.socialaccount.providers.google.provider import GoogleProvider
from allauth.socialaccount.signals import pre_social_login, social_account_added, social_account_updated
from allauth.socialaccount.models import SocialLogin
from allauth.account.models import EmailAddress

# dj-rest-auth imports for JWT and default serializers
from dj_rest_auth.jwt_auth import set_jwt_cookies, unset_jwt_cookies
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

from rest_framework_simplejwt.tokens import RefreshToken

# Get the active User model (which will be Django's default User or a custom one)
User = get_user_model()

# --- Standard Authentication Views (from dj-rest-auth) ---
# These views provide endpoints for traditional email/username and password login/registration
class CustomRegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,) # Allow anyone to register
    serializer_class = RegisterSerializer # Uses dj-rest-auth's default registration serializer
    queryset = User.objects.all() # Queryset for user creation

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # Validate incoming data
        user = serializer.save(request) # Save the new user

        # Generate JWT tokens for the newly registered user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response_data = {
            "user": UserDetailsSerializer(user, context={'request': request}).data, # Serialize user details
            "access_token": access_token,
            "refresh_token": refresh_token,
            "message": "User registered successfully!"
        }

        response = Response(response_data, status=status.HTTP_201_CREATED)
        # Set JWT tokens as HTTP-only cookies for security
        set_jwt_cookies(response, access_token, refresh_token)
        return response

class CustomLoginView(LoginView):
    # This view extends dj-rest-auth's LoginView, which handles authentication
    # and setting JWT cookies by default.
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # The super().post() method already handles setting JWT cookies based on settings
        return response

class CustomLogoutView(LogoutView):
    # This view extends dj-rest-auth's LogoutView, which handles invalidating tokens
    # and unsetting JWT cookies by default.
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # The super().post() method already handles unsetting JWT cookies
        return response

class CustomUserDetailsView(UserDetailsView):
    # This view allows authenticated users to retrieve their own details.
    permission_classes = (IsAuthenticated,) # Only authenticated users can access their profile
    
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user) # Serialize the current authenticated user
        return Response(serializer.data)


# --- Google ID Token Login View ---
# This API view handles login/registration using a Google ID token received from the frontend.
@method_decorator(csrf_exempt, name='dispatch') # Disable CSRF for this endpoint for simplicity in API.
                                               # For production, consider proper CSRF handling or rely solely on JWTs
                                               # for API authentication if not using session-based auth.
class GoogleIDTokenLoginAPIView(APIView):
    permission_classes = (AllowAny,) # Allow unauthenticated access to initiate login

    def post(self, request, *args, **kwargs):
        id_token_str = request.data.get('id_token') # Get the ID token from the request body
        if not id_token_str:
            return Response({"error": "Google ID token not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 1. Verify the ID token with Google's OAuth2 API
            # Get the Google client_id from Django settings
            google_client_id = settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id']
            token_info = id_token.verify_oauth2_token(
                id_token_str, google_requests.Request(), google_client_id
            )

            # 2. Extract user information from the verified token
            email = token_info.get('email')
            first_name = token_info.get('given_name', '')
            last_name = token_info.get('family_name', '')
            # Create a default username from email, ensuring it's unique if necessary later
            username = token_info.get('email', '').split('@')[0]
            google_user_id = token_info['sub'] # 'sub' is the unique Google user ID
            picture_url = token_info.get('picture', '') # Google profile picture URL

            if not email:
                return Response({"error": "Google ID token did not contain an email address."}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic(): # Ensure atomicity for database operations
                # 3. Try to find an existing SocialAccount linked to this Google ID
                social_account = SocialAccount.objects.filter(
                    provider='google', uid=google_user_id
                ).first()

                user = None
                if social_account:
                    # If a social account exists, retrieve the associated Django user
                    user = social_account.user
                else:
                    # If no social account, try to find a Django user by email
                    try:
                        user = User.objects.get(email=email)
                    except User.DoesNotExist:
                        pass # User with this email doesn't exist, will create a new one

                if user:
                    # If a user was found (either via social account or email), ensure social account is linked
                    if not social_account:
                        # Link the existing user to the new social account
                        social_account = SocialAccount.objects.create(
                            user=user,
                            provider='google',
                            uid=google_user_id,
                            extra_data=token_info # Store full token info for future use if needed
                        )
                        # Send allauth signal for social account added
                        social_account_added.send(sender=SocialAccount, request=request, sociallogin=SocialLogin(user=user, account=social_account))
                    else:
                        # If social account already existed, update it (e.g., refresh extra_data)
                        # This signal is useful for custom logic when an account is updated
                        social_account_updated.send(sender=SocialAccount, request=request, sociallogin=SocialLogin(user=user, account=social_account))
                    
                    # Ensure the email address is marked as verified in allauth's EmailAddress model
                    # This is important if allauth's ACCOUNT_EMAIL_VERIFICATION is 'mandatory'
                    if not EmailAddress.objects.filter(user=user, email=email, verified=True).exists():
                         EmailAddress.objects.create(user=user, email=email, primary=True, verified=True)

                else:
                    # 4. If no existing user or social account, create a new Django user and link social account
                    # Generate a random password for the new user, as Google login doesn't provide one.
                    # This password is not used for direct login but is required by Django's User model.
                    generated_password = get_random_string(length=16) # Generates a 16-character random string
                    user = User.objects.create_user(
                        username=username, # You might want to make this unique or use a UUID
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        is_active=True, # New users are active by default
                        password=generated_password # Set the generated random password
                    )
                    social_account = SocialAccount.objects.create(
                        user=user,
                        provider='google',
                        uid=google_user_id,
                        extra_data=token_info # Store the raw token info
                    )
                    # Create and verify the email address for the new user
                    EmailAddress.objects.create(user=user, email=email, primary=True, verified=True)
                    # Send allauth signal for pre social login (useful for custom user data population)
                    pre_social_login.send(sender=SocialLogin, request=request, sociallogin=SocialLogin(user=user, account=social_account))

                # 5. Generate JWT tokens for the authenticated user
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                # Prepare user data for the frontend response
                user_data = UserDetailsSerializer(user, context={'request': request}).data
                user_data['picture'] = picture_url # Add the Google profile picture URL to the response

                response_data = {
                    "user": user_data,
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "message": "Logged in successfully with Google."
                }

                response = Response(response_data, status=status.HTTP_200_OK)
                # Set JWTs as HTTP-only cookies for enhanced security
                set_jwt_cookies(response, access_token, refresh_token)
                return response

        except google_auth_exceptions.InvalidValue as e:
            # Handles errors like 'Token has wrong audience', expired tokens, etc.
            return Response({"error": "Invalid Google ID token or audience mismatch.", "details": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except google_auth_exceptions.GoogleAuthError as e:
            # Catches broader Google authentication errors
            return Response({"error": "Google authentication error.", "details": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            # Catch any other unexpected exceptions for robust error handling
            print(f"Unhandled exception during Google login: {e}")
            import traceback # Import traceback for detailed error logging
            traceback.print_exc() # Print full traceback to console for debugging
            return Response({"error": "An unexpected error occurred during Google login.", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

