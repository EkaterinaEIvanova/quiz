# -*- coding: utf-8 -*-

DEBUG = True

ALLOWED_HOSTS = []

AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiz',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
    }
}

AUTH_USER_MODEL = 'accounts.User'

SECRET_KEY = '73j#q#4mbjtg52)5jijq^#j&=%p15emm)9ztw!@0!4^ytb_hsw'

# MEDIA_ROOT = '/home/ekaterina/projects/garant24/public_html/media'
STATIC_ROOT = '/quiz/static/'

STATICFILES_DIRS = ('quiz/static', )

# STATICFILES_DIRS = (
#     '/home/ekaterina/projects/garant24/garant/static/',
# )

# MANAGERS = [
#     ('Manager1', 'ivanovakate43@gmail.com'),
#     ('Manager2', 'katrinzolo@yandex.ru'),
# ]
#
# ADMINS = [
#     ('Admin1', 'ivanovakate43@gmail.com'),
# ]



CKEDITOR_UPLOAD_PATH = 'content_media'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

DEFAULT_FROM_EMAIL = u'Связь с сайта <mail@webmeg.ru>'
SERVER_EMAIL=u'Связь с сайта <mail@webmeg.ru>'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'mail@webmeg.ru'
EMAIL_HOST_PASSWORD = 'w4jeHu|n8_%xP56/M#NC'
EMAIL_USE_TLS = True

MANAGER_EMAILS = ('t3mp@list.ru', )
THUMBNAIL_DEBUG = True


