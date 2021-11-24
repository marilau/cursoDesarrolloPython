from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ipap',
        'USER': 'postgres',
        'PASSWORD': '1324pg',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
