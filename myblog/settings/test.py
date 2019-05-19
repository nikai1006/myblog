from .base import *

DATABASES ={
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'test',
        'PASSWORD': '123456',
        'HOST': '172.31.28.0',
        'PORT': '3307',
    }
}