# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic import simple

urlpatterns = patterns('planb.feedback.views',
    url(r'^$', 'form', name='feedback_form'),
    url(r'^done/$', simple.direct_to_template,
        dict(template='feedback/feedback_form_done.html'), name='feedback_form_done'),
    )

#EOF