# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField

from planb.core.models import PublishModel


class SubjectConsultation(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u'название'))
    ordering = models.SmallIntegerField(u'Сортировка',  default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = _(u'Тема консультации')
        verbose_name_plural = _(u'Темы консультации')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mayak_consultation_subject', args=[self.id, ])

    def get_archive_url(self):
        return reverse('mayak_consultation_archive_subject', args=[self.id, ])

    def get_archive_consultant(self):
        return self.consiliario_list.published(is_archive=True)


class Consiliario(PublishModel):
    name = models.CharField(max_length=255, verbose_name=_(u'короткое имя'))
    full_name = models.CharField(max_length=255, verbose_name=_(u'полное имя'))
    subject = models.ForeignKey(SubjectConsultation,
                                verbose_name=_(u'специализация'),
                                related_name='consiliario_list',)
    photo = models.ImageField(verbose_name=u'Фотография',
                              upload_to=u'consiliario/photo',
                              help_text=u'изображение обрезаеться до\
                              азмеров 570x380')
    photo_min = models.ImageField(verbose_name=u'маленькая фотография',
                              upload_to=u'consiliario/photo_min',
                              help_text=u'маленькая фотография,\
                              размером 207x138')
    description = RichTextField(u'Описание', blank=True)
    is_archive = models.BooleanField(u'архив', default=True)

    def __unicode__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('mayak_consultant', args=[self.id, ])

    def get_archive_url(self):
        return reverse('mayak_archive_consultant', args=[self.id, ])

    class Meta:
        verbose_name = _(u'консультант')
        verbose_name_plural = _(u'консультанты')


class Question(PublishModel):
    consiliario = models.ForeignKey(
        Consiliario,
        related_name='question_list',
        verbose_name=_(u'Консультант'),
    )
    name = models.CharField(max_length=255, verbose_name=_(u'Имя'))
    email = models.EmailField(
        verbose_name=_(u'email address'),
        max_length=255,
    )
    message = models.TextField(u'сообщение пользователя')
    answer = RichTextField(u'ответ', blank=True)
    date = models.DateTimeField(verbose_name=u'Дата', auto_now_add=True)
    m_time = models.DateTimeField(verbose_name=u'Дата', auto_now=True)

    class Meta:
        ordering = ['-m_time']
        verbose_name = _(u'вопрос постетителя')
        verbose_name_plural = _(u'заданные вопросы')

    def __unicode__(self):
        return u'Вопрос пользователя %s' % self.name
