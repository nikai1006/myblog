from .base import *
LANGUAGE_CODE = 'en-us'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'test',
        'PASSWORD': '123456',
        'HOST': '10.2.17.107',
        'PORT': '3306',
    }
}
