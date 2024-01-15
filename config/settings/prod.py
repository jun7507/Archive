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
        'USER': 'dbmasteruser', #root
        'PASSWORD': 'MoonYang0710*', #사용자의 비밀번호
        'HOST': 'ls-ffe9b51d9f7dcfeacb3d8d12c9e1b5806ab9a156.cze44iokmoyf.ap-northeast-2.rds.amazonaws.com', #공백으로 냅두면 default localhost
        'PORT': '3306' #공백으로 냅두면 default 3306
    }
}
