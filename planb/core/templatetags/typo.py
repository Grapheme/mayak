# -*- coding: utf-8 -*-

from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from planb.core.utils.typo import typo

register = Library()

@register.filter(name='typo')
@stringfilter
def typo_filter(s):
    return mark_safe(typo(s))
typo_filter.is_safe = True