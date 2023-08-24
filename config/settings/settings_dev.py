# settings/local.py
from .settings_common import *
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))



SECRET_KEY = env('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}