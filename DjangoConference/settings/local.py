"""
Set this environment variable
DJANGO_SETTINGS_MODULE=DjangoConference.settings.local
"""

from .base import *  # noqa: F403


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ksu(ubf4l5zti%-z8#=fooukrp0z5frrbwht-17m_6z!03w4s('


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

ALLOWED_HOSTS = ['127.0.0.1']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}