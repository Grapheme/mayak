# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template.context import Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

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


class RadioanchormanForm(forms.Form, BaseFeedbackForm):
    subject = settings.EMAIL_SUBJECT_PREFIX + u'Посетитель сайта пожелал стать радиоведущим'
    template = 'feedback/radioanchorman_email.txt'
    slug = 'radioanchorman'

    name = CharField(label=u'ФИО', max_length=255)
    email = EmailField(label=u'Адрес электронной почты')
    phone = CharField(label=u'Телефон', max_length=42)
    age = forms.IntegerField(label=u'возраст')
    job = CharField(label=u'Место работы', max_length=255)
    hobbies = CharField(label=u'Ваши увлечения', max_length=42)
    petrosian = CharField(label=mark_safe(u'Закончите фразу:<br />Каждую пятницу я...'), widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    face = forms.ImageField(label=u'Фото')

    def save(self, image=None):
        context = self.cleaned_data
        text = render_to_string(self.template, Context(context))
        message = EmailMessage(
            self.subject,
            text,
            settings.DEFAULT_FROM_EMAIL,
            self.get_recipients()
        )
        if image:
            message.attach('.'.join([context['name'], image.name.split('.')[-1]]),
                           image.read(), image.content_type)
        message.send()


class RememberAndProudForm(forms.Form, BaseFeedbackForm):
    subject = settings.EMAIL_SUBJECT_PREFIX + u'Заявка: "Я помню! Я горжусь!'
    template = 'feedback/rememberandproud_email.txt'
    slug = 'rememberandproud'

    name = CharField(label=u'ФИО', max_length=255)
    about = CharField(label=u'О ком хочу рассказать', max_length=765)
    connection = CharField(label=u'Как с вами связаться', max_length=255)
    agree = forms.BooleanField(label=u'Я согласен на обработку данных', required=True, initial=True)

    def save(self, image=None):
        context = self.cleaned_data
        text = render_to_string(self.template, Context(context))
        """message = EmailMessage(
            self.subject,
            text,
            settings.DEFAULT_FROM_EMAIL,
            self.get_recipients()
        )"""
        send_mail(self.subject, text, settings.DEFAULT_FROM_EMAIL, self.get_recipients())
