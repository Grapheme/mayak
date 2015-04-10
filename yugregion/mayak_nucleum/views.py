# -*- coding: utf-8 -*-

import datetime as dt

from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response,\
    get_list_or_404, redirect
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from yugregion.mayak_news.models import News
from yugregion.mayak_nucleum.models import Hospes, Programs, Promo,\
    ProgramsArchive, Staff, Press
from yugregion.mayak_nucleum import forms


def index(request):
    hospes_list = Hospes.objects.published()
    news_last = News.objects.published(date__lte=dt.date.today()).\
        exclude(date=dt.date.today(), time__gte=dt.datetime.now().time())[:10]
    promo_list = Promo.objects.published()
    return render_to_response("nucleum/mayak_index.html", RequestContext(request, {
        'news_last': news_last,
        'hospes_list': hospes_list,
        'promo_list': promo_list,
    }))

def program_list(request):
    program_list = Programs.objects.filter(is_published=True).\
        order_by('-display', 'weight')
    return render_to_response("program/mayak_program_list.html", RequestContext(request, {
        'program_list': program_list,
    }))

def program_detail(request, prog_id=1):
    program = get_object_or_404(Programs, id=prog_id)
    return render_to_response("program/mayak_program_detail.html", RequestContext(request, {
        'program': program,
    }))

def program_archive(request, trans_id='Alai Oli'):
    if trans_id != 'Alai Oli':
        transfer = get_object_or_404(ProgramsArchive, id=trans_id)
    elif ProgramsArchive.objects.count():
        transfer = ProgramsArchive.objects.published()[0]
    else:
        raise Http404
    return render_to_response("program/mayak_program_archive.html", RequestContext(request, {
        'transfer': transfer,
    }))

def about_index(request):
    voices_list = Staff.objects.all()
    press_list = Press.objects.published()
    return render_to_response("nucleum/mayak_about.html", RequestContext(request, {
        'voices_list': voices_list,
        'press_list': press_list,
    }))

def voices_communicate(request, name, surname, id=0):
    voice = get_object_or_404(Staff, name=name, surname=surname)
    voice_list = Staff.objects.exclude(name=name, surname=surname)
    return render_to_response("nucleum/mayak_communicate.html", RequestContext(request, {
        'voice': voice,
        'voice_list': voice_list,
    }))


def voices_communicate(request, name, surname, id=0):
    voice = get_object_or_404(Staff, name=name, surname=surname)
    voice_list = Staff.objects.exclude(name=name, surname=surname)
    return render_to_response("nucleum/mayak_communicate.html", RequestContext(request, {
        'voice': voice,
        'voice_list': voice_list,
    }))


class RadioanchormanForm(FormView):
    template_name = 'nucleum/mayak_radioanchorman.html'
    form_class = forms.RadioanchormanForm
    success_url = 'done/'

    def form_valid(self, form):
        form.save(self.request.FILES['face'])
        return super(RadioanchormanForm, self).form_valid(form)


class RememberAndProud(FormView):
    template_name = 'nucleum/mayak_rememberandproud.html'
    form_class = forms.RememberAndProudForm
    success_url = 'done/'
    
    def get_context_data(self, **kwargs):
        context = super(RememberAndProud, self).get_context_data(**kwargs)
        context['audio_archive'] = Programs.objects.get(id=14).programsarchive_set.published()
        #14
        return context
    
    def form_valid(self, form):
        form.save()
        return super(RememberAndProud, self).form_valid(form)

class RadioanchormanDoneTemplate(TemplateView):
    template_name = 'nucleum/mayak_radioanchorman_done.html'

class RememberAndProudDoneTemplate(TemplateView):
    template_name = 'nucleum/mayak_rememberandproud_done.html'
