from sprinto_proj.settings import *
from dotenv import load_dotenv
import os
import yaml

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

project_folder = os.path.dirname(__file__)
#Commentimg this ass env vars will be injected into aws container from Secret manager
load_dotenv(os.path.join(project_folder, 'local.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    'default': {
        'ENGINE': os.environ['DB_ENGINE'],
        'NAME':  os.environ['DB_NAME'] ,
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
}




