from .base import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NOMBRE'],
        'USER': os.environ['DB_USUARIO'],
        'PASSWORD': os.environ['DB_CLAVE'],
        'HOST': 'localhost',
        'PORT': 5432
    }
}

EMAIL_HOST = os.environ['CORREO_HOST']
EMAIL_HOST_USER = os.environ['CORREO']
EMAIL_HOST_PASSWORD = os.environ['CORREO_CLAVE']