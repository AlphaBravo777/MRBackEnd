import os
import datetime
from secret_key import SECRET_KEY_FROM_FILE, DATABASE_PASSWORD, MICROSERVICES_DB_PASSWORD

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY_FROM_FILE

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['192.168.45.2', 'localhost', '127.0.0.1','192.168.1.2', '192.168.2.26', '192.168.2.24']
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken', #This was added for a test
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'api',
    'graphene_django',
    'django_filters',
    'mrDatabaseModels',
    'mrAdminOffice',
    'mrStock',
    'mrCoreModels',
    # 'graphqlMicroservicesEndpoints'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'meatriteApi.urls'

# Make JWT Auth the default authentication mechanism for Django
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Enables django-rest-auth to use JWT tokens instead of regular tokens.
REST_USE_JWT = True

# Configure the JWTs to expire after 1 hour, and allow users to refresh near-expiration tokens
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=3),
    'JWT_ALLOW_REFRESH': True,
}

GRAPHENE = {
        'SCHEMA': 'meatriteApi.schema.schema'
} 

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'content-disposition',
    'accept-encoding',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'cache-control',
    )


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                # os.path.join(BASE_DIR, '')
                ],
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

WSGI_APPLICATION = 'meatriteApi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meatritedb',
        'USER': 'root',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': '192.168.2.25',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    'orderDetailsMicroService': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mrOrderService',
        'USER': 'microBackends',
        'PASSWORD': MICROSERVICES_DB_PASSWORD,
        'HOST': '192.168.2.25',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    'accountDetailsMicroService': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mrAccountService',
        'USER': 'microBackends',
        'PASSWORD': MICROSERVICES_DB_PASSWORD,
        'HOST': '192.168.2.25',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'meatritedb',
#         'USER': 'root',
#         'PASSWORD': DATABASE_PASSWORD,
#         'HOST': '192.168.2.25',
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'   # set "USE_TZ" = "False" or it will not use the local time, but UTC anyway

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#This is where your app will go and look for the static files
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# LOGGING = {

#     # https://lincolnloop.com/blog/django-logging-right-way/
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'mysite.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'DEBUG',
#         },
#         'mrDatabaseModels': {
#             'handlers': ['file'],
#             'level': 'INFO',
#         },
#     }
# }