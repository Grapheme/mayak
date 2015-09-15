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
        url = u'http://radioshanson.fm'
        times = options.get('t', 5)
        page = None
        for i in range(0, times):
            try:
                #print u'Получаем страницу http://chanson.ru/radio/program/hit-parade/'
                page = html.parse('http://radioshanson.fm/hit-parade/index/')
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
        raw_hitparad_list = page.getroot().find_class('hit-parade-result').pop() #сохранить в ревизию
        if latest_rev:
            if latest_rev.raw_html == html.tostring(raw_hitparad_list):
                print u'Хит-парад не изменился.'
                return
        
        this_rev = HitParadRevision.objects.create(raw_html = html.tostring(raw_hitparad_list))
            
        hitparad_list = raw_hitparad_list.cssselect('tbody tr:not(.spacing)')[0:12]
        for item in hitparad_list:
            pos = item.cssselect('td')[0].text.strip()
            try:
              dynamic = item.cssselect('td')[0].cssselect('img')[0].get('alt').strip()
            except:
              try:
                dynamic = item.cssselect('td')[0].cssselect('span')[0].text_content().strip()
              except:
                dynamic = ''
            img = item.cssselect('td.title')[0].cssselect('img')[0].get('src')
            if img.split('//')[0]=='':
                img = 'http:' + img
            else:
                img = url + img
            song = item.cssselect('td.title')[0].cssselect('span')[1].text.strip()
            singer = item.cssselect('td.title')[0].cssselect('span small')[0].text_content().strip()
            weeks = item.cssselect('td.icon')[0].text_content().strip()
            '''print this_rev
            print pos
            print dynamic
            print img
            print song
            print singer
            print weeks'''
            rev_item = HitParadItem.objects.create(revision = this_rev, pos=pos, dynamic=dynamic, img=img, song=song, singer=singer, weeks=weeks)
        print u'Done.'
        
        