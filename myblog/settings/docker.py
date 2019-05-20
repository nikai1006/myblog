from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'test',
        'PASSWORD': '123456',
        'HOST': 'dockerdb',
        'PORT': '3306',
    }
}
