# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns('yugregion.shanson_advertisers.views',
    url(r'^publicity/$', 'manager_list', name='shanson_manager_list'),
    url(r'^stock/$', 'action_list', name='shanson_action_list'),
    url(r'^stock/(?P<action_id>\d+)$', 'action_detail', name='shanson_advertisers_shanson_action_detail'),
    url(r'^research/$', 'research', name='shanson_advertisers_research'),
    url(r'^partners/$', 'partners', name='mayak_advertisers_partners'),
)

#EOF