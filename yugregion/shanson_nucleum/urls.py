# -*- coding: utf-8 -*-

from django.conf.urls import *

from yugregion.shanson_nucleum.views import ListenerListView


urlpatterns = patterns('yugregion.shanson_nucleum.views',
    url(r'^$', 'index', name='shanson_index'),
    url(r'^hit_parade/$', 'hit_parade', name='show_hit_parade'),
    url(r'^about/$', 'about_index', name='shanson_about'),
    url(r'^communicate/(?P<name>\w+)_(?P<surname>\w+)', 'voices_communicate', name='shanson_nucleum_staff_communicate'),
    url(r'^program/$', 'program_list', name='shanson_program_list'),
    url(r'^program/(?P<prog_id>\d+)/$', 'program_detail', name='shanson_program_detail'),
    url(r'^program/archive/(?P<trans_id>\d+)$', 'program_archive', name='shanson_nucleum_programsarchive_archive'),
    url(r'^program/archive/last/$', 'program_archive', name='shanson_nucleum_programsarchive_archive_last'),
    url(r'^order_song/$', 'order_song', name='order_song'),
    url(r'^listners/$', ListenerListView.as_view(), name='shanson_listner_list'),

    url(r'^news/', include('yugregion.shanson_news.urls')),

    url(r'^advertisers/', include('yugregion.shanson_advertisers.urls')),
)

urlpatterns += patterns('',
    url(r'^manager_connect/$', 'yugregion.shanson_advertisers.views.manager_connect', name='shanson_manager_connect'),
)

#EOF