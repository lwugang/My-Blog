from .base import *

DEBUG = True
ALLOWED_HOSTS = []

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
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}
