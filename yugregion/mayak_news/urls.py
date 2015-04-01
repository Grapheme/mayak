# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import Rss


urlpatterns = patterns('yugregion.mayak_news.views',
    url(r'^$', 'news_index', name='mayak_news_list'),
    url(r'^page_(?P<page>\d+)/$', 'news_index', name='mayak_news_list_page'),
    url(r'^date_(?P<date>[0-9]{4}/[0-9]{2}/[0-9]{2})/$', 'news_date', name='mayak_news_date_list'),
    url(r'^date/json/$', 'news_date_json', name='mayak_news_date_json'),
    url(r'^(?P<news_id>\d+)/$', 'news_show', name='mayak_news_show'),
    url(r'^(?P<news_id>\d+)/more/$', 'day_news_more', name='mayak_day_news_more'),
    url(r'^rss/$', Rss()),
)
