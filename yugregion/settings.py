# -*- coding: utf-8 -*-

from planb.settings import *

SITE_NAME = u'Южный регион'

DEFAULT_FROM_EMAIL = 'noreply@ugradio.fm'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = u'[Южный регион] '

ROOT_URLCONF = 'yugregion.urls'

INSTALLED_APPS += (
    'constance',
    'constance.backends.database',

    'yugregion.mayak_advertisers',
    'yugregion.mayak_news',
    'yugregion.mayak_nucleum',
    'yugregion.mayak_video',
    'yugregion.mayak_consultation',

    'yugregion.shanson_advertisers',
    'yugregion.shanson_nucleum',
    'yugregion.shanson_news',
)

KICK_YEAR = 2011

STATICFILES_DIRS += (
    os.path.join(SITE_ROOT, 'yugregion', 'static'),
)

TEMPLATE_DIRS += (
    os.path.join(SITE_ROOT, 'yugregion', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'yugregion.shanson_nucleum.context_processors.order_song',
	'yugregion.mayak_nucleum.context_processors.mayak_context',
)

ADMIN_TOOLS_MENU = 'yugregion.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'yugregion.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'yugregion.dashboard.CustomAppIndexDashboard'

CONSTANCE_CONFIG = {
    'MAYAK_SHOW_VIDEO_BUTTON': (True, u'показывать кнопку "смотреть" на главной странице Радио "Маяк Ростов"'),
    'MAYAK_SHOW_CONSULTATION_BUTTON': (True, u'показывать кнопку "Online консультации" на главной странице Радио "Маяк Ростов"'),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_SUPERUSER_ONLY = False
# CONSTANCE_DATABASE_CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
# CONSTANCE_DATABASE_CACHE_BACKEND = 'default'
# CONSTANCE_DATABASE_PREFIX = 'constance:yugregion:'

ALLOWED_HOSTS = ['178.62.105.65', 'ugradio.fm']

try:
    from local_settings import *
except ImportError:
    pass

