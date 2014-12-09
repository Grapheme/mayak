# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns('yugregion.mayak_advertisers.views',
    url(r'^publicity/$', 'manager_list', name='mayak_manager_list'),
    url(r'^stock/$', 'action_list', name='mayak_action_list'),
    url(r'^stock/(?P<action_id>\d+)$', 'action_detail', name='mayak_advertisers_action_detail'),
    url(r'^research/$', 'research', name='mayak_advertisers_mayak_research'),
    url(r'^partners/$', 'partners', name='mayak_advertisers_partners'),
)

#EOF