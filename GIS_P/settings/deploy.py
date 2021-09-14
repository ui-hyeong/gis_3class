from .base import *
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'mariadb', #컨테이너이름이랑 같아야함
        'PORT': '3306',
    }
}