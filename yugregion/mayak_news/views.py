# -*- coding: utf-8 -*-

import datetime as dt
import json

from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from yugregion.mayak_news.models import News
from yugregion.mayak_news.utils import add_months


_paginate_per_page = 25

def news_index(request, page=1):
    qs = News.objects.published(date__lte=dt.date.today()).\
        exclude(date=dt.date.today(), time__gte=dt.datetime.now().time())
    paginator = Paginator(qs, _paginate_per_page, 3, True)
    try:
        news_list = paginator.page(page)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    s = news_list[-1].date
    e = news_list[0].date

    news_day_list = qs.filter(
        date__lte=add_months(e, 2),
        date__gte=add_months(s, -1)).dates('date', 'day')

    today = dt.date.today()

    earliest_date = qs.order_by('date')[0].date
    minDate = '%dd' % (earliest_date-today).days

    latest_date = qs.latest('date').date
    maxDate = '%dd' % (latest_date-today).days

    defaultDate = '%dd' % (e-today).days

    return render_to_response("news/mayak_news_list.html", RequestContext(request, {
        'news_list': news_list,
        'news_day_list': news_day_list,
        'minDate': minDate,
        'maxDate': maxDate,
        'defaultDate': defaultDate,
    }))

def news_date(request, date):
    date = dt.datetime.strptime(date, '%Y/%m/%d')
    today = dt.date.today()
    now = dt.datetime.now().time()
    alfa = News.objects.published(date__gt=date).exclude(
        date=today,
        time__gte=now
    ).count()
    page = alfa / _paginate_per_page + 1
    return HttpResponseRedirect(reverse('mayak_news_list_page',
                                kwargs=dict(page=page)))

def news_show(request, news_id):
    today = dt.date.today()
    now = dt.datetime.now().time()
    try:
        news = News.objects.published(id=news_id, date__lte=today).\
            exclude(date=today, time__gte=now)[0]
    except IndexError:
        raise Http404
    day_news_list = News.objects.published(date=news.date).exclude(
        date=today,
        time__gte=now
    ).exclude(id=news.id).order_by('?')[:3]
    return render_to_response("news/mayak_news_show.html", RequestContext(request, {
        'news': news,
        'day_news_list': day_news_list,
    }))


def day_news_more(request, news_id):
    today = dt.date.today()
    now = dt.datetime.now().time()
    try:
        news = News.objects.published(id=news_id, date__lte=today).\
            exclude(date=today, time__gte=now)[0]
    except IndexError:
        raise Http404
    alfa = News.objects.published(date__gt=news.date).exclude(
        date=today,
        time__gte=now
    ).count()
    page = alfa / _paginate_per_page + 1
    return HttpResponseRedirect(reverse('mayak_news_list_page',
                                kwargs=dict(page=page)))


def news_date_json(request):
    if request.method == 'POST':
        date = dt.datetime.strptime(request.POST.get('date'), '%m.%Y')
        date_s = add_months(date, -1)
        date_e = add_months(date, 2)
        qs = News.objects.published(date__lte=date_e, date__gte=date_s).\
            exclude(date=dt.date.today(), time__gte=dt.datetime.now().time()).\
            dates('date', 'day')
        news_day_list = dict()
        for i in qs:
            news_day_list.update({i.strftime('%d.%m.%Y'):{"url":\
            reverse('mayak_news_date_list', args=[i.strftime('%Y/%m/%d')])}})

        return HttpResponse(json.dumps(news_day_list),
            content_type="application/json")
    return Http404()