# -*- coding: utf-8 -*-

from django import template
from django.utils.safestring import mark_safe
from PIL import Image
from django.conf import settings
import re

register = template.Library()

@register.filter
def thriads(value, splitter="&nbsp;"):
    """
    Formats the value into thriads
    """
    s, p = "%s" % value, ""
    if '.' in s:
        s, p = s.split('.')
        p = ".%s" % p
    s = list(s)
    for i in range(len(s)/3):
        s.insert(-i*3-3-i, splitter)
    return mark_safe("".join(s).lstrip(splitter) + p)

thriads.is_safe = True

@register.filter
def round(value):
    return int(value or 0)
    

@register.filter
def get_request(values_dict, exclude=''):
    bits = exclude.split(u',')
    diff = list(set(values_dict.keys()) - set(bits))
    return '&'.join(['%s=%s' % (k, values_dict[k]) for k in diff])


@register.filter
def startswith(fr, t):
    if fr:
        return fr.startswith(t)
    return False
    
@register.filter
def wrap_last_word(s):
    s = s.split(' ')
    
    s.insert(-1, '<span class="nobr">')
    return " ".join(s)
    
    
@register.filter
def height_of_upload(file):
    try:
        image = Image.open(u"%s/%s" % (settings.MEDIA_ROOT, file))
        return image.size[1]
    except:
        return 0
    
@register.filter
def month(date):
  try:
    date = int(date.month)
  except:
    date = 0
  return (
    u'',
    u'января',
    u'февраля',
    u'марта',
    u'апреля',
    u'мая',
    u'июня',
    u'июля',
    u'августа',
    u'сентября',
    u'октября',
    u'ноября',
    u'декабря',
  )[date]
    
@register.filter
def count(num, words):
    num = num and int(num) or 0
    words = words.split(',')
    ret = "%s %%s" % num
    if (abs(num) % 10 == 1) and (abs(num) != 11):
        return ret % words[0]
    elif (abs(num) % 10 in [2,3,4]) and (not abs(num) in [12,13,14]):
        return ret % words[1]
    return ret % words[2]
    
@register.filter
def count_no(num, words):
    num = num and int(num) or 0
    words = words.split(',')
    if (abs(num) % 10 == 1) and (abs(num) != 11):
        return words[0]
    elif (abs(num) % 10 in [2,3,4]) and (not abs(num) in [12,13,14]):
        return words[1]
    return words[2]

@register.filter
def href(url):
    return re.sub(r'(^http:\/\/)|(\/.*?$)', '', url)
    
@register.filter
def mul(i, j):
    return int(i)*int(j)
    
@register.filter
def firstletter(st):
    return unicode(st)[:1]
    
@register.filter
def split(value, slices):
    seq = list(value)
    length = len(seq)
    items_per_slice = length // int(slices)
    slices_with_extra = length % int(slices)
    offset = 0
    for slice_number in xrange(slices):
        start = offset + slice_number * items_per_slice
        if slice_number < slices_with_extra:
            offset += 1
        end = offset + (slice_number + 1) * items_per_slice
        tmp = seq[start:end]
        yield tmp
        
        
@register.filter
def fieldtype(bfield):
    field = bfield
    if hasattr(field, 'field'):
        field = field.field
    return field.widget.__class__.__name__.lower()


@register.filter
def wordbreak(string, arg):
    return re.sub('([^ ]{' + arg + '})', '\\1 ', string)
    
@register.filter
def in_city(s):
    letters = u'цкнгшщзхфвпрлджчсмтб'
    ret = u'в'
    if len(s) > 2 and s[0].lower() in u'вф' and s[1].lower() in letters:
        ret += u'о'
    return ret
    
@register.filter
def discount(n, d):
    return n - n*(d/100.0)