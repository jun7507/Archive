import environ
from .base import *


ALLOWED_HOSTS = ['43.203.89.131']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),  #mysql
        'USER': env('DB_USER'), #root
        'PASSWORD': env('DB_PASSWORD'), #사용자의 비밀번호
        'HOST': env('DB_HOST'), #공백으로 냅두면 default localhost
        'PORT': '5432' #공백으로 냅두면 default 3306
    }
}