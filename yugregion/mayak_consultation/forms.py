# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template.context import Context
from django.template.loader import render_to_string

from planb.core.fields import CharField, EmailField
from planb.feedback.forms import BaseFeedbackForm

from yugregion.mayak_consultation.models import Question


class AskConsultantForm(forms.Form, BaseFeedbackForm):
    subject = u'Посетитель сайта задал вопрос консультанту'
    template = 'feedback/ask_consultant_email.txt'
    slug = 'ask_consultant'

    name = CharField(max_length=255, label=u'Представьтесь, пожалуйста')
    email = EmailField(label=u'Адрес электронной почты')
    text = CharField(placeholder=u'Ваш вопрос',
                     widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))

    def save(self, consultant):
        context = self.cleaned_data
        question = Question.objects.create(
            consiliario = consultant,
            name = context['name'],
            email = context['email'],
            message = context['text'],
            is_published=False,
        )
        text = render_to_string(self.template, Context(context))
        send_mail(
            settings.EMAIL_SUBJECT_PREFIX + self.subject,
            render_to_string(self.template, Context(context)),
            settings.DEFAULT_FROM_EMAIL,
            self.get_recipients()
        )


class BecomeConsultantForm(forms.Form, BaseFeedbackForm):
    subject = u'Посетитель сайта хочет стать консультантом'
    template = 'feedback/become_consultant_email.txt'
    slug = 'become_consultant'

    name = CharField(max_length=255, label=u'Представьтесь, пожалуйста')
    email = EmailField(label=u'Адрес электронной почты')
    phone = CharField(label=u'Телефон', max_length = 42)
    specialization = CharField(max_length=255, label=u'Специализация')
    text = CharField(label=u'Комментарий',
                     widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
