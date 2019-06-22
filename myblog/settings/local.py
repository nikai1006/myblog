from .base import *

LANGUAGE_CODE = 'en-us'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'test',
        'PASSWORD': '123456',
        'HOST': 'nikai.net.cn',
        'PORT': '3306',
    }
}
