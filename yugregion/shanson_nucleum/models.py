# -*- coding: utf-8 -*-

import datetime as dt
import pytils
import random
import re

from django.db import models

from ckeditor.fields import RichTextField

from planb.core.models import PublishModel, PublishManager


DISPLAY_CHOISE = (
    ('main', u'Большое поле'),
    ('extra', u'Маленькое поле(внизу)'),
)

DYNAMIC_CHOISE = (
    ('fa-angle-up', u'Вверх'),
    ('fa-angle-down', u'Вниз'),
    ('fa-angle-right', u'Без изменений'),
)

class HitParadRevision(PublishModel):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    raw_html = models.TextField(u'Сырой html', blank=True, null=True)
    
    def __unicode__(self):
        return u'Ревизия от %s' % (self.date)
    
    class Meta:
        verbose_name = u'Ревизия хитпарада'
        verbose_name_plural = u'Ревизии хитпарада'


class HitParadItem(PublishModel):
    revision = models.ForeignKey(HitParadRevision, verbose_name=u'Ревизия', related_name='revision_set', blank=True, null=True)
    pos = models.PositiveSmallIntegerField(u'Позиция',  default=0, blank=True, null=True)
    img = models.CharField(max_length=762, verbose_name=u'URL картинки', blank=True, null=True)
    singer = models.CharField(max_length=254, verbose_name=u'Исполнитель', blank=True, null=True)
    song = models.CharField(max_length=254, verbose_name=u'Песня', blank=True, null=True)
    weeks = models.PositiveSmallIntegerField(u'Недель в хит-параде',  default=0, blank=True, null=True)
    dynamic = models.CharField(u'Динамика', max_length=254, choices=DYNAMIC_CHOISE, default='none', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.singer, self.song)
    
    class Meta:
        ordering = ('pos',)
    
class Programs(PublishModel):
    title = models.CharField(max_length=255, verbose_name=u'Название')
    anons = RichTextField(u'Анонс', blank=True)
    description = RichTextField(u'Описание', blank=True)
    schedule = RichTextField(u'Расписание', blank=True)
    display = models.CharField(u'Способ отображения', max_length=21, choices=DISPLAY_CHOISE, default='main')
    weight = models.PositiveSmallIntegerField(u'Порядок',  default=0)
    staff = models.ManyToManyField('Staff', through="ProxyShansonStaffPrograms", blank=True, related_name='staff', )

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        verbose_name = u'Программа'
        verbose_name_plural = u'Программы'
        ordering = ('-display', 'title', )

    def get_archive_tree(self):
        b = self.programsarchive_set.all()
        a = dict()
        for y in b.dates('date', 'year'):
            m_l = list()
            for m in b.published(date__year=y.year).dates('date', 'month'):
                d_l = b.published(date__year=y.year, date__month=m.month).order_by('date')
                m_l.append([pytils.dt.ru_strftime(u'%B', date=m), d_l])
            m_l.reverse()
            a.update({y.year: m_l})
        return a

    def get_archive_for_year(self, year):
        return self.programsarchive_set.published(date__year=year)

    def get_photo(self):
        try: return ProgramsPhoto.objects.filter(program=self)[0]
        except: return None

    def get_photo_list(self):
        return ProgramsPhoto.objects.filter(program=self)
    
    def get_earliest_archive_date_for_datapicer(self):
        q = self.programsarchive_set.only('date').published().order_by('date')
        if q.count():
            earliest_date = q[0].date
            today = dt.date.today()
            alfa = earliest_date-today
            return '%dd' % alfa.days
        return None

    def get_latest_archive_date_for_datapicer(self):
        q = self.programsarchive_set.only('date').published()
        if q.count():
            latest_date = q.latest('date').date
            today = dt.date.today()
            alfa = latest_date-today
            return '%dd' % alfa.days
        return None
    
    @models.permalink
    def get_absolute_url(self):
        return ('shanson_program_detail', [str(self.id)])

class ProgramsPhoto(PublishModel):
    program = models.ForeignKey(Programs, verbose_name=u'Программа')
    photo = models.ImageField(verbose_name=u'Фотография', upload_to=u'upload', help_text=u'изображение обрезаеться до размеров 570x380')
    description = RichTextField(u'Описание', blank=True)
    weight = models.PositiveSmallIntegerField(u'Порядок', default=0)

    def __unicode__(self):
        return u'%s' % (self.program)

    class Meta:
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'

class ProgramsArchive(PublishModel):
    program = models.ForeignKey(Programs, verbose_name=u'Программа')
    caption = models.CharField(max_length=255, verbose_name=u'Заголовок передачи')
    date = models.DateField(u'Дата', default=dt.date.today())
    time_s = models.TimeField(u'Время начала', default=dt.datetime.now())
    time_e = models.TimeField(u'Время окончания', default=dt.datetime.now())
    description = RichTextField(u'Описание', blank=True)
    soundcloud = models.CharField(max_length=255, verbose_name=u'Код soundcloud')

    def __unicode__(self):
        return u'%s [%s %s]' % (self.caption, self.date.strftime('%Y-%m-%d'), self.time_s.strftime('%H:%M:%S'))

    @models.permalink
    def get_absolute_url(self):
        s = self.__module__
        r = r'.(\w+).models$'
        app = re.findall(r, s)[0].lower()
        cls = self.__class__.__name__.lower()
        return ('%s_%s_archive' % (app, cls, ), [str(self.id)])

    class Meta:
        ordering = ('-date', '-time_s', )
        verbose_name = u'Передача'
        verbose_name_plural = u'Архив программ'

class ProgramsArchivePhoto(PublishModel):
    program = models.ForeignKey(ProgramsArchive, verbose_name=u'Передача')
    photo = models.ImageField(verbose_name=u'Фотография', upload_to=u'upload', help_text=u'изображение обрезаеться до размеров 570x380')
    description = RichTextField(u'Описание', blank=True)
    weight = models.PositiveSmallIntegerField(u'Порядок', default=0)

    def __unicode__(self):
        return u'Фотография для %s' % (self.program)

    class Meta:
        ordering = ('weight', )
        verbose_name = u'Архивная фотография'
        verbose_name_plural = u'Архивные фотографии'

class Staff(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Имя')
    surname = models.CharField(max_length=255, verbose_name=u'Фамилия')
    name_t = models.CharField(max_length=255, verbose_name=u'Имя', help_text=u'творительный падеж')
    surname_t = models.CharField(max_length=255, verbose_name=u'Фамилия', help_text=u'творительный падеж')
    photo = models.ImageField(verbose_name=u'Фотография', upload_to=u'upload', null=True, blank=True, help_text=u'изображение обрезаеться до размеров 570x380')
    photo_min = models.ImageField(verbose_name=u'Фотография', upload_to=u'upload', null=True, blank=True, help_text=u'маленькая фотография, размером 207x138')
    text = RichTextField(u'Текст', blank=True)
    programs = models.ManyToManyField('Programs', through="ProxyShansonStaffPrograms", blank=True, related_name='programs', )
    weight = models.PositiveSmallIntegerField(u'Порядок', default=0)

    def __unicode__(self):
        return '%s %s' % (self.surname, self.name, )

    def name_surname(self):
        return '%s&nbsp;%s' % (self.name, self.surname, )

    def name_surname_t(self):
        return '%s&nbsp;%s' % (self.name_t, self.surname_t, )

    class Meta:
        verbose_name = u'Голос эфира'
        verbose_name_plural = u'Голоса эфира'
        ordering = ('weight', 'surname', 'name', )

    @models.permalink
    def get_absolute_url(self):
        s = self.__module__
        r = r'.(\w+).models$'
        app = re.findall(r, s)[0].lower()
        cls = self.__class__.__name__.lower()
        return ('%s_%s_communicate' % (app, cls, ), [self.name, self.surname, ])

class ProxyShansonStaffPrograms(models.Model):
    programs = models.ForeignKey(Programs)
    staff = models.ForeignKey(Staff)

    class Meta:
        db_table = 'Proxy_Shanson_Staff_Programs'
        auto_created = Programs

class Promo(PublishModel):
    title = models.CharField(u'название', max_length=200)
    url = models.CharField(u'ссылка', max_length=200, blank=True)
    photo = models.ImageField(u'изображение', upload_to='upload/promo', help_text=u'промо на главной размером 888x384')
    program = models.ForeignKey(Programs, null=True, blank=True, help_text='При выборе программы ссылка на онную генерируется автоматически<br />и имеет приоритет перед заданной вручную ссылкой')
    weight = models.SmallIntegerField(u'порядок', default=0)

    class Meta:
        ordering = ('weight', 'title', )
        verbose_name = u'промо'
        verbose_name_plural = u'промо'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('shanson_index', [])

class Press(PublishModel):
    magazine = models.CharField(u'журнал', max_length=256)
    date = models.CharField(u'дата публикации', max_length=128)
    headline = models.CharField(u'название статьи', max_length=256)
    pdf = models.FileField(u'PDF', upload_to='upload/PDF')
    weight = models.SmallIntegerField(u'порядок', default=0)

    class Meta:
        ordering = ('weight', '-id', )
        verbose_name = u'пресса'
        verbose_name_plural = u'пресса'

    def __unicode__(self):
        return self.headline

class ListenersManager(PublishManager):
    use_for_related_fields = True

    def get_random(self, from_last=20, count=8):
        from_last = count if count > from_last else from_last
        qs = self.get_query_set().published()[:from_last]
        from_last = qs.count() if qs.count() < from_last else from_last
        count = qs.count() if qs.count() < count else count
        qs = [qs[i] for i in random.sample(xrange(from_last), count)]
        return qs


class Listeners(PublishModel):
    photo = models.ImageField(u'изображение', upload_to='listeners')
    m_time = models.DateTimeField(u'дата последнего изменения', auto_now=True )

    objects = ListenersManager()

    class Meta:
        ordering = ('-m_time', )
        verbose_name = u'слушатель'
        verbose_name_plural = u'слушатели'

    def __unicode__(self):
        return u'слушатель #%d' % self.id
