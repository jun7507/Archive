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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python_db',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}