# -*- coding: utf-8 -*-

from os import remove
from shutil import move
import codecs
import os
import sys
import lxml.html as html

from django.core.management.base import NoArgsCommand, BaseCommand, CommandError
from django.conf import settings

from grab import Grab
from grab import error

from ...models import HitParadRevision, HitParadItem

class Command(BaseCommand):
    args = u'<количество попыток соединения по умолчанию 5>'
    help = u'Команда парсящая сайт http://chanson.ru/ и записывающая результат в БД'
    
    #sys.stdout = codecs.open("yugregion/get_hitparad.log", 'a', 'utf-8')
    #sys.stderr = codecs.open("yugregion/get_hitparad.error", 'a', 'utf-8')

    def handle(self, *args, **options):
        url = u'http://chanson.ru'
        times = options.get('t', 5)
        page = None
        for i in range(0, times):
            try:
                print u'Получаем страницу http://chanson.ru/radio/program/hit-parade/'
                page = html.parse('http://chanson.ru/radio/program/hit-parade/')
                print page    
                break
            except:
                if i >= times:
                    print u'%d неудачных попыток' % i
                    raise error.GrabTimeoutError()
                #print u'Соединение с сервером увенчалось фиаско. Ошибка:'
                print sys.exc_info()
        try:
            latest_rev = HitParadRevision.objects.all().order_by('-id')[0]
        except:
            latest_rev = None
        raw_hitparad_list = page.getroot().find_class('d-chart-big-list').pop() #сохранить в ревизию
        if latest_rev:
            if latest_rev.raw_html == html.tostring(raw_hitparad_list):
                print u'Хит-парад не изменился.'
                return
        
        this_rev = HitParadRevision.objects.create(raw_html = html.tostring(raw_hitparad_list))
            
        hitparad_list = raw_hitparad_list.getchildren()[0:12]
        for item in hitparad_list:
            pos = item.find_class('d-chart-big-pos').pop().cssselect('strong').pop().text_content()
            dynamic = item.find_class('d-chart-big-pos').pop().cssselect('i').pop().get('class').split(' ')[1]
            img = item.find_class('d-chart-big-img').pop().cssselect('img').pop().get('src')
            if img.split('//')[0]=='':
                img = 'http:' + img
            else:
                img = url + img
            song = item.find_class('d-chart-big-name').pop().cssselect('strong a').pop().text_content()
            singer = item.find_class('d-chart-big-name').pop().cssselect('div a').pop().text_content()
            weeks = item.find_class('d-chart-big-weeks').pop().cssselect('strong').pop().text_content()
            rev_item = HitParadItem.objects.create(revision = this_rev, pos=pos, dynamic=dynamic, img=img, song=song, singer=singer, weeks=weeks)
        print u'Готово.'
        
        