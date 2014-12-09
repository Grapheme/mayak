# -*- coding: utf-8 -*-

import datetime

from django.template import Library

register = Library()

@register.simple_tag
def copyright_year(start):
    year = datetime.datetime.now().strftime("%Y")
    return year == start and year or start + '&mdash;' + year