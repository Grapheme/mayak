# -*- coding: utf-8 -*-

import os.path

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = lambda *args: os.path.join(SITE_ROOT, *args).replace('\\', '/')

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'planb', 'static'),
)

STATIC_ROOT = os.path.join(SITE_ROOT, 'www', 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LOCAL_MEDIA_ROOT = MEDIA_ROOT
LOCAL_MEDIA_URL = MEDIA_URL

DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))
TEMPLATE_DEBUG = DEBUG

ADMINS = ((os.environ.get('DJANGO_ADMIN_NAME', 'Admin'),
           os.environ.get('DJANGO_ADMIN_EMAIL', 'bugs@plan-b.ru')),)
MANAGERS = ((os.environ.get('DJANGO_MANAGER_NAME', 'Feedback'),
             os.environ.get('DJANGO_MANAGER_EMAIL', 'feedback@plan-b.ru')),)

HR_MANAGERS = [email for (name, email) in MANAGERS]

if DEBUG :
    MANAGERS = ADMINS

DATABASE_SQLITE = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(SITE_ROOT, 'data.db')
}

DATABASES = {
    'default': DATABASE_SQLITE
}

#TIME_ZONE = 'Europe/Moscow'
TIME_ZONE = 'Europe/Minsk'

DATE_INPUT_FORMATS = ('%d-%m-%Y',)

LANGUAGE_CODE = 'ru-RU'

USE_I18N = True

SITE_ID = 1

LOCALE_PATHS = (os.path.join(SITE_ROOT, 'locale'),)

SECRET_KEY = '$-jbx)n2=9s(^b*^ky)x#!um=)j#xbqpk_gx42p3oo8s4usa69'

# JOHNNY_MIDDLEWARE_KEY_PREFIX='jc_bizon'

# DJAPIAN_DATABASE_PATH = os.path.join(SITE_ROOT, 'djapian')
# DJAPIAN_STEMMING_LANG = "ru"

APPEND_SLASH = True

TIME_FORMAT = "H:i"
DATE_FORMAT = "d.m.Y"

THUMBNAIL_DIR = os.path.join(MEDIA_ROOT, 'tmp')
THUMBNAIL_URL = MEDIA_URL + 'tmp/'

YANDEX_KEY = "ABQIAAAAAcw6hZ5eW5YD7hti2lEdChSJ0V14Ok1G6hLQZjuHlVDW_a-HpRRoWtiJ5BGgz4DDLMrszgdmM7IMcg"

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# ADMIN_MEDIA_ROOT = '/usr/local/django/contrib/admin/media/'
# ADMIN_MEDIA_URL = '/static/admin/'
# ADMIN_MEDIA_PREFIX = ADMIN_MEDIA_URL

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',

    'planb.structure.context_processors.current_node',
    'planb.structure.context_processors.site_name',
    'planb.structure.context_processors.breadcrumbs',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'planb.core.middleware.CurrentNodeMiddleware',
    'planb.core.middleware.RequestSiteMiddleware',
)

FILE_UPLOAD_HANDLERS = (
    'planb.core.upload_handlers.MemoryFileUploadHandler',
    'planb.core.upload_handlers.TemporaryFileUploadHandler'
)

ROOT_URLCONF = 'planb.core.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'planb', 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(SITE_ROOT, 'planb', 'fixtures'),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    # 'django.contrib.markup',
    'django.contrib.redirects',
    'django.contrib.staticfiles',

    'mptt',
    'south',
    'ckeditor',

    'planb.core',
    'planb.feedback',
    'planb.gallery',
    'planb.structure',
)

# try:
#     LOCAL_INSTALLED_APPS = INSTALLED_APPS
#     LOCAL_MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES
#     from local_settings import *
#     INSTALLED_APPS += LOCAL_INSTALLED_APPS
#     MIDDLEWARE_CLASSES += LOCAL_MIDDLEWARE_CLASSES
# except ImportError: pass

############
# CKEDITOR #
############
CKEDITOR_UPLOAD_PATH = path(MEDIA_ROOT, 'ck_upload')
CKEDITOR_UPLOAD_PREFIX = MEDIA_URL+'ck_upload/'
if not os.path.exists(CKEDITOR_UPLOAD_PATH):
    os.makedirs(CKEDITOR_UPLOAD_PATH)
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'height': 291,
        'width': 800,
        'toolbar_Full': [
            [
                'Styles',
                'Format',
                'FontSize',
                'Bold',
                'Italic',
                'Underline',
                'Strike',
                'SpellChecker',
                'Undo',
                'Redo',
            ],
            [
                'JustifyLeft',
                'JustifyCenter',
                'JustifyRight',
                'JustifyBlock',
            ],
            [
                'NumberedList',
                'BulletedList',
            ],
            [
                'TextColor',
                'BGColor',
            ],
            [
                'HorizontalRule',
                'SpecialChar',
                'Image',
                'Smiley',
            ],
            [
                'Source',
            ],
            [
                'Maximize',
            ],
        ],
        'filebrowserWindowWidth': 940,
        'filebrowserWindowHeight': 725,
    },
}

ADMIN_TOOLS_THEMING_CSS = 'css/admin.css'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
