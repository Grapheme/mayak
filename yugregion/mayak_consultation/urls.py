# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'yugregion.mayak_consultation.views',
    url(r'^$', 'consultation', name='mayak_consultation' ),

    url(r'^subject/(?P<subject>\d+)/$', 'consultation',
        name='mayak_consultation_subject' ),

    url(r'^consultant/(?P<id>\d+)/$', 'consultant',
        name='mayak_consultant' ),
    url(r'^consultant/(?P<id>\d+)/ask/$', 'consultant_ask',
        name='mayak_consultant_ask' ),
    url(r'^consultant/(?P<id>\d+)/done/$', 'consultant_ask_done',
        name='mayak_consultant_ask_done' ),

    url(r'^archive/$', 'archive', name='mayak_consultation_archive' ),
    url(r'^archive/subject/(?P<subject>\d+)/$', 'consultation',
        {'archive': True}, name='mayak_consultation_archive_subject' ),
    url(r'^archive/consultant/(?P<id>\d+)/$', 'consultant',
        {'archive': True}, name='mayak_archive_consultant' ),

    url(r'^become/$', 'consultant_become',
        name='mayak_consultant_become' ),
    url(r'^become/done/$', 'consultant_become_done',
        name='mayak_consultant_become_done' ),
)
