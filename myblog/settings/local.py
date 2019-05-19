from .base import *

LANGUAGE_CODE = 'en-us'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'test',
        'PASSWORD': '123456',
        'HOST': '192.168.100.2',
        'PORT': '3306',
    }
}
