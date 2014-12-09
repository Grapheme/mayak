# -*- coding: utf-8 -*-

import datetime as dt

from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from yugregion.shanson_news.models import News


_paginate_per_page = 8

def news_index(request, page=1):
    news_list = News.objects.published(date__lte=dt.date.today()).exclude(date=dt.date.today(), time__gte=dt.datetime.now().time())
    paginator = Paginator(news_list, _paginate_per_page, 1, True)
    try:
        news_list = paginator.page(page)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    return render_to_response("news/shanson_news_list.html", RequestContext(request, {'news_list': news_list, }))


def news_show(request, news_id):
    try:
        news = News.objects.published(id=news_id, date__lte=dt.date.today()).exclude(date=dt.date.today(), time__gte=dt.datetime.now().time())[0]
    except IndexError:
        raise Http404
    day_news_list = News.objects.published(date=news.date).exclude(date=dt.date.today(), time__gte=dt.datetime.now().time()).exclude(id=news.id).order_by('?')[:3]
    return render_to_response("news/shanson_news_show.html", RequestContext(request, {
        'news': news,
        'day_news_list': day_news_list,
    }))


def day_news_more(request, news_id):
    try:
        news = News.objects.published(id=news_id, date__lte=dt.date.today()).exclude(date=dt.date.today(), time__gte=dt.datetime.now().time())[0]
    except IndexError:
        raise Http404
    alfa = News.objects.published(date__gt=news.date).exclude(date=dt.date.today(), time__gte=dt.datetime.now().time()).count()
    page = alfa / _paginate_per_page + 1
    return HttpResponseRedirect(reverse('shanson_news_list_page', kwargs=dict(page=page)))
