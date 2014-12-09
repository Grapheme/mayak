# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings

from planb.core.fields import CharField, EmailField
from planb.feedback.forms import BaseFeedbackForm

class ManagerConnectForm(forms.Form, BaseFeedbackForm):
    subject = u'Посетитель сайта желает связаться с менеджером'
    template = 'feedback/manager_connect_email.txt'
    slug = 'manager_connect'

    name = CharField(max_length = 42, placeholder=u'Представьтесь')
    organization = CharField(placeholder=u'Организация', max_length = 42)
    phone = CharField(placeholder=u'Контактный номер', max_length = 42)
    email = EmailField(placeholder=u'Электронная почта')
    text = CharField(placeholder=u'Текст', widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))

#EOF