from .base import *


ALLOWED_HOSTS = ['43.203.89.131']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = True

# env = environ.Env()
# environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = "django-insecure-!)*$!urvee%7ol4iopz3*4+g2c7vll@_b_xi7zan39i%zo%*8v"

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python_db',  #mysql
        'USER': 'yangjaejun', #root
        'PASSWORD': 'Epwkqb#3515', #사용자의 비밀번호
        'HOST': 'localhost', #공백으로 냅두면 default localhost
        'PORT': '3308' #공백으로 냅두면 default 3306
    }
}