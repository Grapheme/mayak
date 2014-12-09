# -*- coding: utf-8 -*-

import datetime as dt

from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView

from yugregion.shanson_nucleum.forms import OrderSongForm
from yugregion.shanson_nucleum.models import Programs, Staff, Press\
    , Promo, ProgramsArchive, Listeners
from yugregion.shanson_news.models import News


def index(request):
    promo_list = Promo.objects.published()
    news_list = News.objects.published(date__lte=dt.date.today()).exclude(date=dt.date.today(), time__gte=dt.datetime.now().time())[:4]
    listeners_list = Listeners.objects.get_random()
    return render_to_response("nucleum/shanson_index.html", RequestContext(request, {
        'promo_list': promo_list,
        'news_list': news_list,
        'listeners_list': listeners_list,
    }))

def hit_parade(request):
    return render_to_response("nucleum/shanson_hit_parade.html", RequestContext(request, {
    }))

def program_list(request):
    program_list = Programs.objects.filter(is_published=True).order_by('-display', 'weight')
    return render_to_response("program/shanson_program_list.html", RequestContext(request, {'program_list': program_list, }))

def program_detail(request, prog_id):
    program = get_object_or_404(Programs, id=prog_id)
    return render_to_response("program/shanson_program_detail.html", RequestContext(request, {'program': program, }))

def program_archive(request, trans_id='Alai Oli'):
    if trans_id != 'Alai Oli':
        transfer = get_object_or_404(ProgramsArchive, id=trans_id)
    elif ProgramsArchive.objects.count():
        transfer = ProgramsArchive.objects.published()[0]
    else:
        raise Http404
    return render_to_response("program/shanson_program_archive.html", RequestContext(request, {
        'transfer': transfer,
    }))

def about_index(request):
    voices_list = Staff.objects.all()
    press_list = Press.objects.published()
    return render_to_response("nucleum/shanson_about.html", RequestContext(request, {
        'voices_list': voices_list,
        'press_list': press_list,
        'parent': 'shanson_layout.html',
    }))

def voices_communicate(request, name, surname, id=0):
    voice = get_object_or_404(Staff, name=name, surname=surname)
    voice_list = Staff.objects.exclude(name=name, surname=surname)
    return render_to_response("nucleum/shanson_communicate.html", RequestContext(request, {
        'voice': voice,
        'voice_list': voice_list,
    }))

def order_song(request):
    order_form = OrderSongForm(request.POST or None)
    if order_form.is_valid():
        order_form.save()
    context = RequestContext(request)
    context['order_form'] = order_form
    response = render_to_response('feedback/order_song_form.html', context)
    response.set_cookie('order_song_result', order_form.is_valid())
    return response

class ListenerListView(ListView):
    model = Listeners
    template_name= 'nucleum/listeners_list.html'
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.published(*args, **kwargs)