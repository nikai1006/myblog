from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myblog',  # 数据库名字
        'USER': 'test',  # 用户名
        "PASSWORD": '123456',  # 自己的密码
        "HOST": '',
        'PORT': 5432,
    }
}
