from .base import *
# Database

env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True :
    line = local_env.readline()
    if not line :
        break

    line = line.replace('\n', '')    # 한줄로
    start = line.find('=')        #= 이 있는 곳을 찾기
    key = line[:start]                 #  왼쪽부분을 키  SECRET_KEY = 'django-insecure-ez14bcuso741!155ys$8h1v6kl-gs$ok-)8k56ll*6jz!cr404'
    value = line[start+1:]             #  오른쪽을 밸류
    env_list[key] = value



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']


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