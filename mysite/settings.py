"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
# import structlog

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vi77+sktt=o-1=jj-=huz!-fy4rtq6o7!5-g^8(m3c8)4=9sb2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
ALLOWED_HOSTS = ['127.0.0.1', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
    'photo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # djangoの構造化ロギング
    # 'django_structlog.middlewares.RequestMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Uploaded files
# MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, './media')

# 構造化ロギングの設定

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "json_formatter": {
#             "()": structlog.stdlib.ProcessorFormatter,
#             "processor": structlog.processors.JSONRenderer(),
#         },
#         "plain_console": {
#             "()": structlog.stdlib.ProcessorFormatter,
#             "processor": structlog.dev.ConsoleRenderer(),
#         },
#         "key_value": {
#             "()": structlog.stdlib.ProcessorFormatter,
#             "processor": structlog.processors.KeyValueRenderer(
#                 key_order=[
#                     'timestamp', 'level', 'event', 'logger'
#                 ]
#             ),
#         },
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "formatter": "plain_console",
#         },
#         "json_file": {
#             "class": "logging.handlers.WatchedFileHandler",
#             "filename": "logs/json.log",
#             "formatter": "json_formatter",
#         },
#         "flat_line_file": {
#             "class": "logging.handlers.WatchedFileHandler",
#             "filename": "logs/flat_line.log",
#             "formatter": "key_value",
#         },
#     },
#     "loggers": {
#         "django_structlog": {
#             "handlers": ["console", "flat_line_file", "json_file"],
#             "level": "INFO",
#         },
#         "django_structlog_demo_project": {
#             "handlers": ["console", "flat_line_file", "json_file"],
#             "level": "INFO",
#         },
#     }
# }

# structlog.configure(
#     processors=[
#         structlog.stdlib.filter_by_level,
#         structlog.processors.TimeStamper(fmt="iso"),
#         structlog.stdlib.add_logger_name,
#         structlog.stdlib.add_log_level,
#         structlog.stdlib.PositionalArgumentsFormatter(),
#         structlog.processors.StackInfoRenderer(),
#         structlog.processors.format_exc_info,
#         structlog.processors.UnicodeDecoder(),
#         structlog.processors.ExceptionPrettyPrinter(),
#         structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
#     ],
#     context_class=structlog.threadlocal.wrap_dict(dict),
#     logger_factory=structlog.stdlib.LoggerFactory(),
#     wrapper_class=structlog.stdlib.BoundLogger,
#     cache_logger_on_first_use=True,
# )
