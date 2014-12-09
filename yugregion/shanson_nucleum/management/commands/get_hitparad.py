# -*- coding: utf-8 -*-

from os import remove
from shutil import move
import codecs
import os
import sys

from django.core.management.base import NoArgsCommand, BaseCommand, CommandError
from django.conf import settings

from grab import Grab
from grab import error

class Command(BaseCommand):
    args = u'<количество попыток соединения по умолчанию 5>'
    help = u'Команда парсящая сайт http://chanson.ru/ и записывающая результат в файл'

    sys.stdout = codecs.open("yugregion/get_hitparad.log", 'a', 'utf-8')
    sys.stderr = codecs.open("yugregion/get_hitparad.error", 'a', 'utf-8')

    def handle(self, *args, **options):
        times = options.get('t', 5)
        hit = Grab()
        for i in range(0, times):
            try:
                print u'Подключение к http://chanson.ru/programmes/shansongoda/'
                hit.go('http://chanson.ru/programmes/shansongoda/')
                break
            except error.GrabTimeoutError:
                if i >= times:
                    print u'%d неудачных попыток' % i
                    raise error.GrabTimeoutError()
                print u'Соединение с сервером увенчалось фиаско ошибку GrabTimeoutError возвратил модуль.'
        table = hit.xpath('//table[@class="hitparad"]')
        tr_list = table.getchildren()[1:]

        h_file = codecs.open('yugregion/templates/includes/$hitparad.html', 'w', 'utf-8')
        i_h_file = codecs.open('yugregion/templates/includes/$index_hitparad.html', 'w', 'utf-8')
        for i, tr in enumerate(tr_list):
            # позиция #
            position = tr.getchildren()[0].text_content().replace('\n','').replace('\t','').replace('  ',' ')
            # ссылка на фотографию #
            photo = 'http://chanson.ru%s' % tr.getchildren()[2].getchildren()[0].get('src')
            # исполнитель #
            performer = tr.getchildren()[3].text_content().replace('\n','').replace('\t','').replace('  ',' ')
            # трек #
            track = tr.getchildren()[4].text_content().replace('\n','').replace('\t','').replace('  ',' ')
            # недель в хит-параде #
            weeks = tr.getchildren()[5].text_content().replace('\n','').replace('\t','').replace('  ',' ')
            # динамика #
            d = tr.getchildren()[1].getchildren()[0].get('alt')
            if d in [u'Улучшилось', ]:
                dynamics = {
                    'image': 'images/up.png',
                    'alt': u'Улучшилось',
                }
            elif d in [u'Ухудшилось', ]:
                dynamics = {
                    'image': 'images/down.png',
                    'alt': u'Ухудшилось',
                }
            else:
                dynamics = {
                    'image': 'images/up-top.png',
                    'alt': u'Не изменилось',
                }

            h_file.write('''
<tr>
    <td>%s</td>
    <td><span class="img-holder"><img src="%s" width="60" height="60" alt="%s" /><span class="shadow"></span></span></td>
    <td>%s</td>
    <td>%s</td>
    <td class="num">%s</td>
    <td><img src="%s%s" width="20" height="27" alt="%s" /></td>
</tr>''' % (
                position,
                photo,
                performer,
                performer,
                track,
                weeks,
                settings.STATIC_URL,
                dynamics.get('image'),
                dynamics.get('alt')
            ))
            if i < 5:
                i_h_file.write('''
<tr>
    <td>%s</td>
    <td><span class="img-holder"><img src="%s" width="60" height="60" alt="%s" /><span class="shadow"></span></span></td>
    <td>%s</td>
    <td>%s</td>
    <td class="num">%s</td>
    <td><img src="%s%s" width="20" height="27" alt="%s" /></td>
</tr>''' % (
                    position,
                    photo,
                    performer,
                    performer,
                    track,
                    weeks,
                    settings.STATIC_URL,
                    dynamics.get('image'),
                    dynamics.get('alt')
                ))
            print u'%s. %s - %s' % (position, performer, track, )
        h_file.close()
        i_h_file.close()
        if os.path.exists('yugregion/templates/includes/hitparad.html'):
            remove('yugregion/templates/includes/hitparad.html')
        if os.path.exists('yugregion/templates/includes/index_hitparad.html'):
            remove('yugregion/templates/includes/index_hitparad.html')
        move('yugregion/templates/includes/$hitparad.html', 'yugregion/templates/includes/hitparad.html')
        move('yugregion/templates/includes/$index_hitparad.html', 'yugregion/templates/includes/index_hitparad.html')