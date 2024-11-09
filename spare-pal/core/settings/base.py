"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$)zzb#5(m+f%=ul#s2(jf*@32)-^f_q3*3x0%1)c6esl3a+o%a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#################################
#################################
#####* My Custom Settings *######
#################################
#################################

import os

from decouple import config, Csv

# Auth User model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Secret Key
SECRET_KEY = config('SECRET_KEY', default='django-insecure-rtt5va)ck5%&rpi5x!n%^rj9lkzzg3vk3k5mo!#0p$6vvv5oq=')

# Debug
DEBUG = config("DEBUG", default=False, cast=bool)

# Allowed Hosts
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=['*'])

# Application definition
INSTALLED_APPS += [
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt', # Uncomment when using JWT
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'dj_rest_auth.registration',
    'corsheaders',
    'drf_spectacular',

    # Local apps
    # 'customers',
    # 'deliveries',
    # 'logistics',
    # 'orders',
    # 'parts',
    'apps.companies',
    'apps.accounts',
]

# Middleware
# Middleware
MIDDLEWARE += [
    # Cors middleware
    'corsheaders.middleware.CorsMiddleware',
    # Allauth middleware
    'allauth.account.middleware.AccountMiddleware',
    # Locale middleware
    'django.middleware.locale.LocaleMiddleware',
]

# Locale Settings
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, '../', 'locale')]

# Static files (CSS, JavaScript, Images) and Media files
STATIC_URL = 'static/' # url to access static files for both development and production
MEDIA_URL = '/media/' # url to access user uploaded files for both development and production
STATIC_ROOT = os.path.join(BASE_DIR, "../", "static") # store static files
MEDIA_ROOT = os.path.join(BASE_DIR, "../", "media") # store user uploaded files

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    # allauth specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    # Needed to login by username in Django admin, regardless of allauth
    'django.contrib.auth.backends.ModelBackend',
    # Email login

]

# Identify user using email
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # Tell allauth that the User model has no username field
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_VERIFICATION = 'none' # Override the above setting to configure for social login(No email verification required, as the email is already verified by the social provider)
# activate the email account once the user clicks on the link
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication', # Session Based Authentication
        'rest_framework.authentication.TokenAuthentication', # Token Based Authentication
        'rest_framework_simplejwt.authentication.JWTAuthentication', # JWT Authentication
        # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication', # JWT Cookie Authentication
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# JWT settings
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=90),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=180),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Rest auth settings
REST_AUTH = {
    # Serializer settings
    'LOGIN_SERIALIZER': 'apps.accounts.api.serializers.CustomUserLoginSerializer',
    'REGISTER_SERIALIZER': 'apps.accounts.api.serializers.CustomUserRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'apps.accounts.api.serializers.CustomUserDetailsSerializer',

    # Password Settings
    'OLD_PASSWORD_FIELD_ENABLED': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,

    # from the library demo # Uncomment when using JWT
    # 'SESSION_LOGIN': True,
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'email-access-token',
    'JWT_AUTH_REFRESH_COOKIE': 'email-refresh-token',
    'JWT_AUTH_HTTPONLY': False,
}


# DRF Spectacular settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'SparePal API',
    'DESCRIPTION': 'API for SparePal project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

# Site ID
SITE_ID = 1

# Set the default from email address
DEFAULT_FROM_EMAIL = 'no-reply@sparepal.com'

# write custom url link that is to be sent via email
ACCOUNT_ADAPTER = "apps.accounts.api.views.CustomAccountAdapter"

# Celery
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("REDIS_BACKEND")
