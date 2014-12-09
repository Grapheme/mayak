# -*- coding: utf-8 -*-

import datetime as dt

from django.db import models

from ckeditor.fields import RichTextField

from planb.core.models import PublishModel


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    description = RichTextField(verbose_name=u'Описание', blank=True)
    weight = models.PositiveSmallIntegerField(u'Порядок',  default=0)

    def __unicode__(self):
        return u'%s' % (self.title, )

    class Meta:
        ordering = ('weight', '-id', )
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

class Gallery_Img(PublishModel):
    gallery = models.ForeignKey(Gallery)
    img = models.FileField(verbose_name=u'Фотография', upload_to='upload/Gallery_Img')
    description = RichTextField(verbose_name=u'Описание', blank=True)
    weight = models.PositiveSmallIntegerField(u'Порядок',  default=0)

    def __unicode__(self):
        return u'%s - %s [%s]' % (self.gallery, self.description[:60], self.is_published)

    class Meta:
        ordering = ('weight', 'id', )
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

#EOF