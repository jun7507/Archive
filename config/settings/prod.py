from .base import *

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['43.200.2.89']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python_db',
        'USER': 'dbmasteruser',
        'PASSWORD': 'MoonYang0710*',
        'HOST': 'ls-ffe9b51d9f7dcfeacb3d8d12c9e1b5806ab9a156.cze44iokmoyf.ap-northeast-2.rds.amazonaws.com',  # 또는 데이터베이스 호스트 주소
        'PORT': '3306',       # 또는 데이터베이스 포트 번호
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
    },
}
