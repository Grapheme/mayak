# -*- coding: utf-8 -*-

import re

from django import template

from yugregion.shanson_nucleum.models import Staff, Programs

register = template.Library()

class VoicesBroadcast(template.Node):

    def __init__(self, var_name,):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = Staff.objects.all()
        return ''

@register.tag
def get_shanson_voices(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    var_name = m.groups()[0]
    return VoicesBroadcast(var_name)

class StaffList(template.Node):

    def __init__(self, prog, voice, var_name):
       self.prog, self.voice, self.var_name = prog, voice, var_name

    def render(self, context):
        context[self.var_name] = Staff.objects.filter(programs=context[self.prog]).exclude(id=context[self.voice].id)
        return ''

@register.tag
def get_shanson_staff_list_without(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    m = re.search(r'(\w+) (\w+) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    prog, voice, var_name = m.groups()
    return StaffList(prog, voice, var_name)