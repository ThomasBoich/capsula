from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2q6k&jwj$i0fdt(rso0x7(+1yuca_#*23s2fk9hb+1&0tf+(1!"

## DEBUG OFF-ON
DEBUG = True

## LOCALHOST
ALLOWED_HOSTS = []

## LINK SQLLITE3
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]