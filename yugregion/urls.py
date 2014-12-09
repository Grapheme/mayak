# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from planb.core.urls import urlpatterns

local_urlpatterns = patterns('',
    url(r'^mayak/', include('yugregion.mayak_nucleum.urls')),
    url(r'^shanson/', include('yugregion.shanson_nucleum.urls')),
)

urlpatterns = local_urlpatterns + urlpatterns