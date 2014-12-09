# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from yugregion.mayak_consultation.models import Consiliario, Question,\
    SubjectConsultation
from yugregion.mayak_consultation.forms import AskConsultantForm,\
    BecomeConsultantForm


def _get_context_data(archive=False):
    context = dict()
    subject_list = Question.objects.published(
        consiliario__is_archive=archive
    ).exclude(answer='').values_list('consiliario__subject_id', flat=True).\
        distinct()
    context['subject_list'] = SubjectConsultation.objects.\
        filter(id__in=subject_list)

    context['consultant_list'] = Consiliario.objects.published(is_archive=archive)
    return context


def consultation(request, subject=None, archive=False):
    context = RequestContext(request, _get_context_data(archive))
    kwargs = dict({
        'consiliario__is_archive': archive,
    })
    if subject:
        kwargs.update(dict(consiliario__subject_id=subject))
        context['subject'] = get_object_or_404(SubjectConsultation,
            id=subject,
        )
    qs = Question.objects.published(**kwargs).exclude(answer='')

    paginator = Paginator(qs, 10, 3, True)
    page = request.GET.get('page', 1)
    try:
        question_list = paginator.page(page)
    except EmptyPage:
        question_list = paginator.page(paginator.num_pages)

    context['archive'] = archive
    context['question_list'] = question_list
    template = 'consultation/mayak_consultation.html'
    return render_to_response(template, context)


def consultant(request, id, archive=False):
    consult = get_object_or_404(Consiliario, id=id, is_published=True)
    context = RequestContext(request, _get_context_data(archive))

    page = request.GET.get('page', 1)
    qs = Question.objects.published(consiliario=consult).exclude(answer='')
    paginator = Paginator(qs, 10, 3, True)
    try:
        question_list = paginator.page(page)
    except EmptyPage:
        question_list = paginator.page(paginator.num_pages)

    context['archive'] = archive
    context['consult'] = consult
    context['question_list'] = question_list
    template = 'consultation/mayak_consultant.html'
    return render_to_response(template, context)


def consultant_ask(request, id):
    consult = get_object_or_404(Consiliario, id=id, is_archive=False,
                                is_published=True)

    form = AskConsultantForm(request.POST or None)
    if form.is_valid():
        form.save(consultant=consult)
        return HttpResponseRedirect(reverse('mayak_consultant_ask_done', args=[consult.id]))

    context = RequestContext(request, _get_context_data())

    context['consult'] = consult
    context['form'] = form
    template = 'consultation/mayak_consultant_form.html'
    return render_to_response(template, context)


def consultant_ask_done(request, id):
    context = RequestContext(request, _get_context_data())
    context['consult'] = get_object_or_404(Consiliario, id=id, is_archive=False,
                                           is_published=True)

    template = 'consultation/mayak_consultant_done.html'
    return render_to_response(template, context)


def consultant_become(request):
    form = BecomeConsultantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('mayak_consultant_become_done'))

    context = RequestContext(request, _get_context_data())

    context['form'] = form
    template = 'consultation/mayak_become_consultant_form.html'
    return render_to_response(template, context)


def consultant_become_done(request):
    context = RequestContext(request, _get_context_data())

    template = 'consultation/mayak_become_consultant_done.html'
    return render_to_response(template, context)


def archive(request):
    context = RequestContext(request, _get_context_data(True))

    subject_list = Question.objects.published(
        consiliario__is_archive=True
    ).exclude(answer='').values_list('consiliario__subject_id', flat=True).\
        distinct()
    context['subject_list'] = SubjectConsultation.objects.\
        filter(id__in=subject_list)

    context['archive'] = True
    template = 'consultation/mayak_consultant_archive.html'
    return render_to_response(template, context)
