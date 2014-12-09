# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models

from ckeditor.fields import RichTextField

from planb.core.models import PublishModel


class News(PublishModel):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    date = models.DateField(verbose_name=u'Дата')
    time = models.TimeField(verbose_name=u'Время')
    anons = RichTextField(verbose_name=u'Анонс', blank=True)
    text = RichTextField(verbose_name=u'текст', blank=True)
    photo = models.ImageField(verbose_name=u'Фотография', upload_to='upload', help_text=u'изображение обрезаеться до размеров 627x405')

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ('-date', '-time', )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('shanson_news_show', [self.id])
