# -*- coding: utf-8 -*-

from utils.thumbnails import get_thumbnail
import datetime

from django import forms
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from django.utils.translation import ugettext_lazy as _

class ReadOnlyWidget(forms.Widget):
    ''' http://www.djangosnippets.org/snippets/937/ '''
    def __init__(self, original_value, display_value):
        self.original_value = original_value
        self.display_value = display_value
        super(ReadOnlyWidget, self).__init__()

    def render(self, name, value, attrs=None):
        if self.display_value is not None:
            return unicode(self.display_value)
        return unicode(self.original_value)

    def value_from_datadict(self, data, files, name):
        return self.original_value

class SplitDateField(forms.MultiValueField):
    default_error_messages = {
        'invalid_date': _(u'Enter a valid date.'),
    }

    def __init__(self, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (
            forms.CharField(error_messages={'invalid': errors['invalid_date']}),
            forms.CharField(error_messages={'invalid': errors['invalid_date']}),
            forms.CharField(error_messages={'invalid': errors['invalid_date']}),
        )
        super(SplitDateField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            # Raise a validation error if time or date is empty
            # (possible if SplitDateTimeField has required=False).
            if data_list[0] in (None, u'None') or data_list[1] in (None, u'None') or data_list[2] in (None, u'None'):
                return None
            return datetime.date(int(data_list[2]),int(data_list[1]),int(data_list[0]))
        return None


class SplitDateWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.Select(attrs=attrs, choices=([(None, '--')] + [(day, day) for day in range(1,32)])), \
            forms.Select(attrs=attrs, choices=([(None, '--')] + [(month, month) for month in range(1,13)])), \
            forms.Select(attrs=attrs, choices=([(None, '----')] + [(year, year) for year in range(1942,1999)])),
        )
        super(SplitDateWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]



class SplitPhoneField(forms.MultiValueField):
    default_error_messages = {
        'invalid': _(u'Enter a valid phone.'),
    }

    def __init__(self, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (
            forms.CharField(error_messages={'invalid': errors['invalid']}),
            forms.CharField(error_messages={'invalid': errors['invalid']}),
        )
        super(SplitPhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in (None, '') or data_list[1] in (None, ''):
                raise forms.ValidationError(self.error_messages['invalid'])
            return "-".join(["+7"] + data_list)
        return ""

class SplitPhoneWidget(forms.MultiWidget):
    def __init__(self, attrs1=None, attrs2=None):
        widgets = (
            forms.TextInput(attrs=attrs1),
            forms.TextInput(attrs=attrs2),
        )
        super(SplitPhoneWidget, self).__init__(widgets)

    def decompress(self, value):
        if value:
            return value.split("-")[1:]
        return ["", ""]

    def format_output(self, rendered_widgets):
        return u'<span style="float: left; padding-left: 10px; height: 1px;"></span>'.join([u'<span class="text">%s</span>' % f for f in rendered_widgets])

class ThumbImageFieldFile(ImageFieldFile):
    """
    See ImageWithThumbsField for usage example
    """
    def make_thumbs(self):
        if not self.field.presets:
            return

        for preset in self.field.presets.values():
            get_thumbnail(self, preset)

            # TODO: make_thumbnail, storage
            #self.storage.delete(thumb_name)
            #self.storage.save(thumb_name, thumb_content)

    def save(self, name, content, save=True):
        super(ThumbImageFieldFile, self).save(name, content, save)
        self.make_thumbs()

    def delete(self, save=True):
        # TODO: delete
        #if self.field.presets:
        #    for size in self.field.presets:
        #        self.storage.delete(self.thumb_name(size))
        super(ThumbImageFieldFile, self).delete(save)

class ThumbImageField(ImageField):

    attr_class = ThumbImageFieldFile

    def __init__(self, verbose_name=None, name=None, width_field=None,
            height_field=None, presets=[], **kwargs):
        self.width_field, self.height_field = width_field, height_field
        self.presets = presets
        super(ImageField, self).__init__(verbose_name, name, **kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^planb\.core\.forms\.ThumbImageField"])
except ImportError:
    pass