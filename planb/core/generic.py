# -*- coding: utf-8 -*-

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

class RequestForm(forms.Form):
    def __init__(self, request, **kwargs):
        self.request = request
        if request.method == 'POST':
            kwargs.update({'data': request.POST, 'files': request.FILES})
        super(RequestForm, self).__init__(**kwargs)
    
    def save(self):
        raise NotImplementedError
    
    def redirect_url(self):
        return 'done/'
    
    def cancel_url(self):
        return '/'

def request_form(request, form_class, template_name, extra_context=None, **form_kwargs):
    assert issubclass(form_class, RequestForm)

    form = form_class(request, **form_kwargs)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(form.redirect_url())

    context = extra_context and extra_context.copy() or {}
    context.update({'form': form})

    return render_to_response(template_name, context, RequestContext(request))