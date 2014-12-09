# -*- coding: utf-8 -*-

import random

from django import template
from django.db import models

register = template.Library()

class ModelsList(template.Node):
    def __init__(self, qs, result):
        self.qs = qs
        self.result = result
    def render(self, context):
        context.update({self.result: self.qs})
        return ''

def _get_with_type(object_tuple):
    val = object_tuple[1]

    try:
        object_tuple[1] = int(val)
    except:
        if val == 'True' or val == 'False':
            object_tuple[1] = (val == 'True')
        elif val == 'None':
            object_tuple[1] = None
        else:
            object_tuple[1] = val
    return object_tuple

def _get_content(appname, modelname, filters=None):
    model = models.get_model(appname, modelname)
    if model is None:
        raise template.TemplateSyntaxError('can not find model %s.%s' % \
                                           (appname, modelname))
    object_list = model.objects.all()
    if filters:
        object_list = object_list.filter(
            *[_get_with_type(fltr.split(':', 1)) for fltr in filters.split(';')])

    return object_list

@register.tag
def model_list(parser, token):
    tokens = token.split_contents()
    if len(tokens) == 4:
        _, appname, modelname, result = tokens
        filters = ''
    elif  len(tokens) == 5:
        _, appname, modelname, filters, result = tokens
    else:
        raise template.TemplateSyntaxError

    return ModelsList(_get_content(appname, modelname, filters), result)

@register.tag
def model_object(parser, token):
    tokens = token.split_contents()
    if len(tokens) == 5:
        _, appname, modelname, index, result = tokens
        filters = None
    elif  len(tokens) == 6:
        _, appname, modelname, filters, index, result = tokens
    else:
        raise template.TemplateSyntaxError

    try:
        return ModelsList(_get_content(appname, modelname, filters)[int(index)], result)
    except IndexError:
        return ModelsList([], result)

class GetRandom(template.Node):
    def __init__(self, qs, result):
        self.qs = qs
        self.result = result

    def render(self, context):
        try:
            model_list = list(self.qs)
            index = random.randint(0, len(model_list)-1)
            result = (index, model_list[index])
            context.update({self.result: result}) 
            return ''
        except template.VariableDoesNotExist:
            return ''

@register.tag
def random_object(parser, token):
    tokens = token.split_contents()
    if len(tokens) == 4:
        _, appname, modelname, result = tokens
        filters = ''
    elif  len(tokens) == 5:
        _, appname, modelname, filters, result = tokens
    else:
        raise template.TemplateSyntaxError

    return GetRandom(_get_content(appname, modelname, filters), result)

class GetRandomCount(template.Node):
    def __init__(self, qs, count, result):
        self.qs = qs
        self.count = template.Variable(count)
        self.result = result

    def render(self, context):
        try:
            qs = self.qs.order_by('?')
            count = self.count.resolve(context)
            if len(qs) > count:
                result = qs[:count] 
            else:  				
                result = qs
            context.update({self.result: result}) 
            return ''
        except template.VariableDoesNotExist:
            return ''

@register.tag
def random_list(parser, token):
    tokens = token.split_contents()
    if len(tokens) == 5:
        _, appname, modelname, count, result = tokens
        filters = ''
    elif  len(tokens) == 6:
        _, appname, modelname, filters, count, result = tokens
    else:
        raise template.TemplateSyntaxError

    return GetRandomCount(_get_content(appname, modelname, filters), count, result)