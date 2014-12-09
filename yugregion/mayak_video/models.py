# -*- coding: utf-8 -*-

import datetime as dt

from django.db import models
from django.utils.translation import ugettext_lazy as _

from planb.core.models import PublishModel

from yugregion.mayak_nucleum.models import Programs


class Video(PublishModel):
    program = models.ForeignKey(Programs, verbose_name=u'Программа')
    title = models.CharField(max_length=255, verbose_name=_(u'Название'))
    date = models.DateField(u'Дата', default=dt.date.today())
    time_s = models.TimeField(u'Время начала', default=dt.datetime.now())
    time_e = models.TimeField(u'Время окончания', default=dt.datetime.now())
    video = models.TextField(max_length=255, verbose_name=_(u'Код видео youtube'))
    text = models.TextField(verbose_name=_(u'текст'), blank=True)

    class Meta:
        verbose_name = _(u'Видео')
        verbose_name_plural = _(u'Видео архив')
        ordering = ['-date', '-time_s', ]

    def __unicode__(self):
        return u'%s [%s %s]' % (self.title, self.date.strftime('%Y-%m-%d'), self.time_s.strftime('%H:%M:%S'))

    @models.permalink
    def get_absolute_url(self):
        return ('mayak_nucleum_program_video_archive_archive', [self.id])
