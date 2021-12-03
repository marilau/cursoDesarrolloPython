import os
from .base import *

DEBUG = True

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

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
