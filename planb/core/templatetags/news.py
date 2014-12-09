# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.inclusion_tag('includes/news_sections.html')
def news_archive_sections(sections, current_year):
    return {'sections': sections, 'current_year': current_year}