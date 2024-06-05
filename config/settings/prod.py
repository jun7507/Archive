from .base import *

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ml', # 데이터베이스 이름
        'USER': 'yangjaejun', # 데이터베이스 사용자 이름
        'PASSWORD': 'password',
        'HOST': '192.168.0.2',  # 또는 데이터베이스 호스트 주소
        'PORT': '5432',       # PostgreSQL 기본 포트 번호
    },
}
