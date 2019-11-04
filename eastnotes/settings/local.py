from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'djangoblog',
    #     'USER': 'root',
    #     'PASSWORD': 'root',
    #     'PORT': '3306',
    #     'HOST': 'localhost',
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
