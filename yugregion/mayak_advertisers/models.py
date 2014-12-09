# -*- coding: utf-8 -*-

from pytils.dt import ru_strftime
import datetime as dt
import pytils

from django.core.urlresolvers import reverse
from django.db import models

from ckeditor.fields import RichTextField

from planb.core.models import PublishModel
from planb.gallery.models import Gallery
from planb.core.utils.thumbnails import get_thumbnail


class Managers(PublishModel):
    name = models.CharField(max_length=20, verbose_name=u'Имя')
    surname = models.CharField(max_length=21, verbose_name=u'Фамилия')
    post = models.CharField(max_length=128, verbose_name=u'Должность')
    photo = models.ImageField(verbose_name=u'Фотография', upload_to=u'upload', null=True, blank=True, help_text=u'фотография размером 119x119')
    text = RichTextField(u'Текст', blank=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length = 20)
    email = models.EmailField(blank=True)
    weight = models.PositiveSmallIntegerField(u'Порядок',  default=0)

    def __unicode__(self):
        return '%s %s' % (self.surname, self.name, )

    def name_surname(self):
        return '%s %s' % (self.name, self.surname, )

    class Meta:
        verbose_name = u'Партнёр'
        verbose_name_plural = u'Партнёры'
        ordering = ('weight', 'title', )

    def photo_thumb(self):
        if self.photo:
            return u'<img src="%s" height="50"/>' % get_thumbnail(self.photo.path, **{'out_size': [0, 50], 'crop': True})
        else:
            return '(none)'
    photo_thumb.short_description = u'Предпросмотр'
    photo_thumb.allow_tags = True

    class Meta:
        verbose_name = u'Менеджер'
        verbose_name_plural = u'Менеджеры'
        ordering = ('weight', )

class Action(PublishModel):
    title = models.CharField(u'Заголовок', max_length=200)
    date_s = models.DateField(u'Дата начала', default=dt.date.today())
    date_e = models.DateField(u'Дата конца', default=dt.date.today())
    anons = RichTextField(u'Анонс', blank=True)
    description = RichTextField(u'Текст', blank=True)
    gallery = models.ForeignKey(Gallery, verbose_name=u'галерея', blank=True, null=True)
    weight = models.SmallIntegerField(u'Порядок',  default=0)

    def __unicode__(self):
        return self.title

    def get_date(self):
        if self.date_s.year != self.date_e.year:        date_format = u'%d&nbsp;%B %Y&nbsp;&mdash; '
        elif self.date_s.month != self.date_e.month:    date_format = u'%d&nbsp;%B &mdash; '
        elif self.date_s.day != self.date_e.day:        date_format = u'%d &mdash; '
        else:                                           date_format = u''
        s = pytils.dt.ru_strftime(date_format, date=self.date_s, inflected=True)
        e = pytils.dt.ru_strftime(u'%d&nbsp;%B %Y', date=self.date_e, inflected=True)
        return u'%s%s' % (s, e)

    class Meta:
        verbose_name = u'Акция'
        verbose_name_plural = u'Акции'
        ordering = ('weight', 'date_s', )

class Mayak_Research(PublishModel):
    title = models.CharField(u'Название', max_length=200)
    embed_code = models.CharField(u'Embed code', max_length=200)

    class Meta:
        verbose_name = u'Исследование'
        verbose_name_plural = u'Исследования'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mayak_advertisers_mayak_research')

class Partners(PublishModel):
    title = models.CharField(u'Название', max_length=200)
    logo = models.ImageField(u'Логотип', upload_to='upload/partners/', null=True, blank=True, help_text=u'логотип размером 193x236')
    weight = models.PositiveSmallIntegerField(u'Порядок',  default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Партнёр'
        verbose_name_plural = u'Партнёры'
        ordering = ('weight', 'title', )

    def logo_thumb(self):
        if self.logo:
            return u'<img src="%s" height="50"/>' % get_thumbnail(self.logo.path, **{'out_size': [0, 50], 'crop': True})
        else:
            return '(none)'
    logo_thumb.short_description = u'Предпросмотр'
    logo_thumb.allow_tags = True