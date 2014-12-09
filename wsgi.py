import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'yugregion.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

