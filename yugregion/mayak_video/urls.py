# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('yugregion.mayak_video.views',
    url(r'^$', 'program_video_archive', name='mayak_nucleum_program_video_archive_archive_last'),
    url(r'^(?P<pk>\d+)$', 'program_video_archive', name='mayak_nucleum_program_video_archive_archive'),
    url(r'^last/$', 'program_video_archive', name='mayak_nucleum_program_video_archive_archive_last'),
)
