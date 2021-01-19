from. import *


ALLOWED_HOSTS = ['www.rb-dev-web.fr', 'rb-dev-web.fr']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
