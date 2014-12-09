# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^404/', lambda request: TemplateView.as_view(template_name="404.html")(request)),
    # тут бы указать mime type
    url(r'^robots\.txt$', lambda request: TemplateView.as_view(template_name='robots.txt')(request)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ckeditor/', include('ckeditor.urls')),
)

code = "|".join([code for code, _ in settings.LANGUAGES])

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^test/(?P<template>.*)',
            lambda request, template: TemplateView.as_view(template_name=template)(request))
    )
    rexp = r'^' + settings.MEDIA_URL.lstrip('/') + '(?P<path>.*)$'
    args = {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
    urlpatterns += patterns('', url(rexp, 'django.views.static.serve', args))

urlpatterns += patterns('',
    url(r'^images/(?P<field_val>.*)/', 'planb.structure.views.uploadedfile', {'field': 'slug'}),
    url(r'^images/(?P<field>pk|slug)/(?P<field_val>.*)\.(?P<img_w>\d+)x(?P<img_h>\d+)/', 'planb.structure.views.uploadedfile'),
    url(r'^images/(?P<field>pk|slug)/(?P<field_val>.*)/', 'planb.structure.views.uploadedfile', name='core_uploads_url'),
    url(r'^images/(?P<field_val>.*)/', 'planb.structure.views.uploadedfile', dict(field='slug')),

    url(r'^(?P<path>.*)', 'planb.structure.views.structurenode'),
    )

#EOF