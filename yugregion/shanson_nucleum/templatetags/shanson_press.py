# -*- coding: utf-8 -*-

import re

from django import template

from yugregion.shanson_nucleum.models import Press

register = template.Library()

class PressBroadcast(template.Node):

    def __init__(self, var_name,):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = Press.objects.published()
        return ''

@register.tag
def get_shanson_press(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    var_name = m.groups()[0]
    return PressBroadcast(var_name)