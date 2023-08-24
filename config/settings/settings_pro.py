from .settings_common import *
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


SECRET_KEY = env('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'mydatabase',
        'USER':'djangouser',
        'PASSWORD':'0000',
        'HOST':'localhost',
        'PORT':'5432',
    }
}