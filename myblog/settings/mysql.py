
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWORD': 'nikai123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}