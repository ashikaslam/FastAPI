# backend/settings.py

import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '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' # CHANGE THIS IN PRODUCTION
DEBUG = True
ALLOWED_HOSTS = ['*'] # For development, allows all hosts. Restrict in production.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # Required by allauth

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'dj_rest_auth',
    'dj_rest_auth.registration', # Provides default registration endpoints

    # django-allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # Google social provider

    # Your custom API app
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Must be before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Allauth middleware
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # `allauth` requires this
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication', # Use JWT for API auth
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny', # Adjust as needed for specific endpoints
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer', # Useful for testing in browser
    ]
}

# CORS Headers settings
CORS_ALLOW_ALL_ORIGINS = True # WARNING: For development only!
# In production, specify your React app's domain:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000", # Your React app's development server
#     "https://your-frontend-domain.com",
# ]
CORS_ALLOW_HEADERS = [
    "accept", "accept-encoding", "authorization", "content-type", "dnt",
    "origin", "user-agent", "x-csrftoken", "x-requested-with",
]
CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT",]
CORS_ALLOW_CREDENTIALS = True # Important for sending cookies/session (if used)

# django-allauth settings
SITE_ID = 1 # Required by allauth

ACCOUNT_AUTHENTICATION_METHOD = "username_email" # Allow login with username or email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none" # For simplicity in this example. Use "mandatory" in production.
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_LOGOUT_ON_GET = False # Prevent accidental logout on GET request

# dj-rest-auth settings
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'my-app-auth', # Name of the JWT cookie
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token', # Name of the refresh token cookie
    'JWT_AUTH_SAMESITE': 'Lax', # Or 'None' with SECURE_PROXY_SSL_HEADER if cross-site
    'TOKEN_MODEL': None, # Crucial: tells dj-rest-auth not to use Django's Token model
    # dj-rest-auth will use its default serializers for UserDetails, Login, Register
}

# JWT settings (from djangorestframework-simplejwt)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), # Access token valid for 60 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7), # Refresh token valid for 7 days
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Google Social Account Providers (Client ID and Secret from Google Cloud Console)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            # IMPORTANT: Use the Client ID for your "Web application" OAuth 2.0 Client ID
            'client_id': '865209583510-ncomqfrmdd3b5jma73kn3id5hk8e1894.apps.googleusercontent.com',
            # IMPORTANT: Use the Client Secret for your "Web application" OAuth 2.0 Client ID
            'secret': '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',
            'key': '' # This is usually not needed for Google
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline', # Important for getting refresh tokens
        },
        'OAUTH_PKCE_ENABLED': True, # Recommended for security
    }
}