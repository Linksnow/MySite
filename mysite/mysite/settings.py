"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加 apps 目录
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rhis)#7e-ac6kbf4y$tzj5ad$6c=ct52v=s7s0$37tnuorrtme'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['119.3.19.102']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # for allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.baidu',
    
    # for crispy
    'crispy_forms',

    # for blog
    'blog',

    # for myauth
    'myauth',
    
]

# 重载auth_model
AUTH_USER_MODEL = 'myauth.Myuser'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1

# allauth 配置

#作用是登陆时可以用用户名也可以用邮箱
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
#作用时注册时，邮箱是必备的。
ACCOUNT_EMAIL_REQUIRED = True
#指定登陆成功后的跳转路径 默认是 /accounts/profile/
LOGIN_REDIRECT_URL = "/"
#禁用注册邮箱验证
ACCOUNT_EMAIL_VERIFICATION='none'
#登出直接退出，不用确认
ACCOUNT_LOGOUT_ON_GET=True


EMAIL_HOST = 'smtp.163.com'            #配置smtp地址
EMAIL_HOST_USER = 'example@163.com'              #配置邮箱地址 
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxx'                  #配置授权码，注意是授权码，不是邮箱密码
EMAIL_PORT = 465                                         #端口号
EMAIL_USE_SSL = True                                #指定SSL发送
EMAIL_FROM = "example"                            #可以指定邮件发件人
DEFAULT_FROM_EMAIL = 'example<example@163.com>'  


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'templates')],
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
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
