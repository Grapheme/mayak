# -*- coding: utf-8 -*-

import re

from django.template import Library

register = Library()

@register.filter
def urlizer(url):
    '''
    Фильтр заменяющий недопустимые символы в строке, для использования её в url
    '''
    URL_REPLACE_LIST = (
        (' ', '_'),
    )
    for k in URL_REPLACE_LIST:
        url = url.replace(*k)
        print url
    return url