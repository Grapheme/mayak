# -*- coding: utf-8 -*-

from django.conf import settings
from django import forms
from django.core.mail import EmailMessage
from django.template.context import Context
from django.template.loader import render_to_string

from planb.core.fields import CharField, EmailField
from planb.feedback.forms import BaseFeedbackForm


class OrderSongForm(forms.Form, BaseFeedbackForm):
    subject = settings.EMAIL_SUBJECT_PREFIX + u'Посетитель сайта заказал песню'
    template = 'feedback/order_song_email.txt'
    slug = 'order_song'

    name = CharField(label=u'Представьтесь', placeholder=u'Представьтесь', max_length = 42)
    artist = CharField(label=u'Исполнитель', placeholder=u'Исполнитель', max_length = 42)
    track = CharField(label=u'Название песни', placeholder=u'Название песни', max_length = 42)
    email = EmailField(label=u'Электронная почта', placeholder=u'Электронная почта', required=False)
    comment = CharField(label=u'Комментарии', placeholder=u'Комментарии', widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}), required=False)

    def save(self):
        context = self.cleaned_data
        text = render_to_string(self.template, Context(context))
        message = EmailMessage(
            self.subject,
            text,
            settings.DEFAULT_FROM_EMAIL,
            self.get_recipients())
        message.send()
