from .base import *

DEBUG = False
ALLOWED_HOSTS = ["123.206.218.63"]

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MyBlog',
        'USER': 'root',
        'PASSWORD': 'lwg123456',
        'HOST': '123.206.218.63',
        'CHARSET': 'utf8',
        'COLLATION': 'utf8',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


