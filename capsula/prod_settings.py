import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-sdjkfhsjkdrh3472q6k&jwj$i0fdt(rso0x7(+1yuca_#*23s2fk9hb+1&0tf+(1!"

## DEBUG ON-OFF
DEBUG = False

## ADRESS VPS
ALLOWED_HOSTS = []

## LINKS POSTGRESQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "name_post",
        "USER": "user_name",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432"
    }
}

## ROOT STATIC FILES
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')