#!/usr/bin/env python
#coding:utf-8
import os
import ConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=vs8ojnndz@-aj19k-&3n4msv+k)ov3-qd7p3#q&9ysfdfdu5#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
LOGIN_REDIRECT_URL = "/"

#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True
#SENDFILE_BACKEND = 'sendfile.backends.development'


#python manage.py makemigrations
#python manage.py migrate
#
# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CMDB',
    'deploy_manager',
    'saltjob',
    'nested_inline',
    'mptt',
    'rest_framework',
    'tools_manager',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ops.urls'

SUIT_CONFIG = {

    'ADMIN_NAME': u'K2DATA后台管理系统',
    'MENU': (
        'sites',
        #{'label': 'blog', 'icon':'icon-cog', 'models': ('suit.price', )},
        # Rename app and set icon
        {'app': 'cmdb', 'label': u'资产管理', 'icon':'icon-lock'},
        {'app': 'deploy_manager', 'label': u'发布管理', 'icon':'icon-cog'},
        {'app': 'tools_manager', 'label': u'工具管理', 'icon':'icon-star'},

        # Reorder app models
        {'app': 'suit', 'models': ('price',)},
    ),
    'SEARCH_URL': '/admin/user',

    # Parameter also accepts url name
    'SEARCH_URL': 'admin:auth_user_changelist',

    # Set to empty string if you want to hide search from menu
    'SEARCH_URL': ''
}



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'cmdb',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
    }
}
'''


cf = ConfigParser.ConfigParser()
cf.read("ops/config.ini")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': cf.get("db","name"),
        'USER': cf.get("db","user"),
        'PASSWORD':cf.get("db","pass"),
        'HOST': cf.get("db","host"),
        'PORT': cf.get("db","port"),
    }
}




# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
PACKAGE_PATH = os.path.join("ops")

CRONJOBS = [
    ('*/30 * * * *', 'saltjob.cron.scanHostJob')
]

# '''REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     )
# }'''
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}




'''
SALT_REST_URL = 'https://10.1.10.176:8000/'
SALT_USER = 'admin'
SALT_PASSWORD = 'admin123'

'''

SALT_REST_URL=cf.get('salt','salt_url')
SALT_USER=cf.get('salt','salt_user')
SALT_PASSWORD=cf.get('salt','salt_passwd')
