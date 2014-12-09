# -*- coding: utf-8 -*-

import datetime as dt

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template.context import Context
from django.template.loader import render_to_string

from planb.feedback.models import FeedbackFormManager

class BaseFeedbackForm(object):
    subject = u'Сообщение с сайта'
    template = 'feedback/feedback_email.txt'
    slug = 'feedback'

    def get_recipients(self):
        try:
            form_manager = FeedbackFormManager.objects.get(slug=self.slug)
            return form_manager.email.all().values_list('email', flat=True)
        except FeedbackFormManager.DoesNotExist:
            return list()

    def save(self):
        context = self.cleaned_data
        text = render_to_string(self.template, Context(context))
        send_mail(
            settings.EMAIL_SUBJECT_PREFIX + self.subject, 
            render_to_string(self.template, Context(context)), 
            settings.DEFAULT_FROM_EMAIL, 
            self.get_recipients()
        )

    def output_1(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(field)s %(errors)s</div>',
            error_row = u'%s',
            row_ender = '</div>',
            help_text_html = u'<p class="hefp-text">%s</p>',
            errors_on_separate_row = False
        )

class FeedbackForm(forms.Form, BaseFeedbackForm):
    name = forms.CharField(label=u'Ваше имя', max_length=80)
    email = forms.EmailField(label=u'Ваш e-mail')
    message = forms.CharField(label=u'Сообщение', widget=forms.Textarea)

class ModelFeedbackForm(forms.ModelForm, BaseFeedbackForm):
    def save(self, commit=True):
        context = self.cleaned_data
        send_mail(
            settings.EMAIL_SUBJECT_PREFIX + self.subject, 
            render_to_string(self.template, Context(context)), 
            settings.DEFAULT_FROM_EMAIL, 
            self.get_recipients()
        )
        return super(ModelFeedbackForm, self).save(commit)