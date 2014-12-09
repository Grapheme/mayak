# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('yugregion.shanson_news.views',
    url(r'^$', 'news_index', name='shanson_news_list'),
    url(r'^page_(?P<page>\d+)/$', 'news_index', name='shanson_news_list_page'),
    url(r'^(?P<news_id>\d+)/$', 'news_show', name='shanson_news_show'),
    url(r'^(?P<news_id>\d+)/more/$', 'day_news_more', name='shanson_day_news_more'),
)
