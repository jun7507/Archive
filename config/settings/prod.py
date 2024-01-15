from .base import *

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['43.203.89.131']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python_db',  #mysql
        'USER': 'root', #root
        'PASSWORD': '1234', #사용자의 비밀번호
        'HOST': 'localhost', #공백으로 냅두면 default localhost
        'PORT': '3306' #공백으로 냅두면 default 3306
    }
}