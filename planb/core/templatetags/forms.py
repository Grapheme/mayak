# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

DEFAULT_TEMPLATE = getattr(settings, 'FORMS_DEFAULT_TEMPLATE', 'includes/field.html')

register = template.Library()

def render_field(field, tmpl=None):
    ''' Фильтр для вывода одного поля формы 
        Коротко: {{ myform.field|field }}
        С указанием шаблона: {{ myform.field|field:"forms/field.html" %}
    '''

    tmpl = tmpl or DEFAULT_TEMPLATE
    return render_to_string(tmpl, template.Context({'field': field}))

register.filter('field', render_field)

def render_fieldset(form, args):
    ''' Фильтр для вывода набора полей формы.
        Синтаксис такой: {{ myform|fieldset:"field1,field2" }}
        Можно указать персональный шаблон для некоторых или всех полей:
        {{ myform|fieldset:"field1:forms/field1.html,field2" }}
    '''
    result = ''
    
    for bits in (s.split(':', 1) for s in args.split(',')):
        fn, ft = bits[0], (len(bits) == 2) and bits[1] or None
        result += render_field(form[fn], ft)
    
    return mark_safe(result)

register.filter('fieldset', render_fieldset)

@register.filter
def fieldtype(bfield):
    field = bfield
    if hasattr(field, 'field'):
        field = field.field
    return field.widget.__class__.__name__.lower()

@register.filter
def get_other_field(form, field):
    if (field + '_other') in form.fields:
        return form[field + '_other']
    return None

@register.filter
def is_other_field(field):
    return field.name.endswith('_other')

@register.filter
def get_header(form, field):
    if hasattr(form, 'get_header'):
        return form.get_header(field.name)
    return None