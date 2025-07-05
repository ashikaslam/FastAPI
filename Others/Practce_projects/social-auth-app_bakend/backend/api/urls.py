# backend/api/urls.py
from django.urls import path
from .views import (
    CustomRegisterView, CustomLoginView, CustomLogoutView, CustomUserDetailsView,
    GoogleIDTokenLoginAPIView
)
from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    # Standard dj-rest-auth endpoints
    path('register/', CustomRegisterView.as_view(), name='rest_register'),
    path('login/', CustomLoginView.as_view(), name='rest_login'),
    path('logout/', CustomLogoutView.as_view(), name='rest_logout'),
    path('profile/', CustomUserDetailsView.as_view(), name='rest_user_details'), # Renamed from 'user/' to 'profile/' to match React

    # JWT token management
    path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Custom Google ID Token Login endpoint
    path('google/id-token/', GoogleIDTokenLoginAPIView.as_view(), name='google_id_token_login'),
]