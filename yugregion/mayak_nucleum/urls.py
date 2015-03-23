# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from yugregion.mayak_nucleum.views import RadioanchormanForm, RadioanchormanDoneTemplate, RememberAndProud, RememberAndProudDoneTemplate


urlpatterns = patterns(
    'yugregion.mayak_nucleum.views',

    url(r'^$', 'index', name='mayak_index'),
    url(r'^about/$', 'about_index', name='mayak_about'),
    url(r'^communicate/(?P<name>\w+)_(?P<surname>\w+)',
        'voices_communicate', name='mayak_nucleum_staff_communicate'),

    url(r'^consultation/',
        include('yugregion.mayak_consultation.urls')),

    url(r'^program/$', 'program_list', name='mayak_nucleum_programs_list'),
    url(r'^program/(?P<prog_id>\d+)/$', 'program_detail',
        name='mayak_nucleum_programs_detail'),
    url(r'^program/archive/$', 'program_archive'),
    url(r'^program/archive/(?P<trans_id>\d+)$', 'program_archive',
        name='mayak_nucleum_programsarchive_archive'),
    url(r'^program/archive/last/$', 'program_archive',
        name='mayak_nucleum_programsarchive_archive_last'),
    url(r'^program/video_archive/', include('yugregion.mayak_video.urls')),

    url(r'^news/', include('yugregion.mayak_news.urls')),

    url(r'^advertisers/', include('yugregion.mayak_advertisers.urls')),

    url(r'^radioanchorman_form/$', RadioanchormanForm.as_view(),
        name='radioanchorman_form'),
    url(r'^radioanchorman_form/done/$', RadioanchormanDoneTemplate.as_view(),
        name='radioanchorman_form_done'),
    url(r'^rememberandproud/$', RememberAndProud.as_view(), name='rememberandproud_form'),
    url(r'^rememberandproud/done/$', RememberAndProudDoneTemplate.as_view(), name='rememberandproud_form_done'),
)

urlpatterns += patterns(
    '',

    url(r'^manager_connect/$',
        'yugregion.mayak_advertisers.views.manager_connect',
        name='mayak_manager_connect'),
)
