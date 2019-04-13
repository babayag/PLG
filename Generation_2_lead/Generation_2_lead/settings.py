"""
Django settings for Generation_2_lead project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^&t3gh&dfqr-)3z@eu+s+1+c4thall6rh3(hk&w_n9n)e=z%bz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['41.205.23.64', '41.205.23.64:8000', 'localhost:3000', '47.99.121.32', '127.0.0.1', 'localhost']



# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',  # new
    'djoser',
    #'knox',
    'social_django',
    'rest_social_auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        #'knox.auth.TokenAuthentication',
    ],
}

#json web token lifetime expire
SIMPLE_JWT={
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=2),
    'AUTH_HEADER_TYPES': ('JWT',),
}

#add config for social endpoint

SOCIAL_AUTH_TOKEN_STRATEGY = 'djoser.social.token.jwt.TokenStrategy'
SOCIAL_AUTH_ALLOWED_REDIRECT_URIS = [
    'http://127.0.0.1:8000/dashboard'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # new
    'django.middleware.common.CommonMiddleware',  # new
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    '127.0.0.1:8000'
    '41.205.23.64:8080',
    '127.0.0.1:8000',
)

ROOT_URLCONF = 'Generation_2_lead.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend' , 'build'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
SOCIAL_AUTH_POSTGRES_JSONFIELD = True
WSGI_APPLICATION = 'Generation_2_lead.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
      'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'leadmehome',
         'USER': 'postgres',
         'PASSWORD': 'Bonjour6',
         'HOST': '127.0.0.1',
         'PORT': '5432',
    }
}

SOUTH_TESTS_MIGRATE = False

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#json web token lifetime expire

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'frontend', 'build', 'static'),
]

AUTH_USER_MODEL = 'example.SpaUser'
