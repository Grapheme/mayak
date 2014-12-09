# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from planb.core.utils.thumbnails import get_thumbnail


class AdminImageWidget(AdminFileWidget):
    """
    Виджет добавляет представление картинки размером Х * 100
    """
    def render(self, name, value, attrs=None):
        output = []
        file_name = str(value)
        if file_name:
            file_path = '%s%s' % (settings.MEDIA_URL, file_name)
            thumb = u'<img src="%s" alt="%s" />' % (get_thumbnail('%s/%s' % (settings.MEDIA_ROOT, file_name), **{'out_size': ('0', '100'), 'crop': True}), file_name)
            output.append('<a target="_blank" href="%s">%s</a>' % (file_path, thumb, ))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class FileUploadForm(forms.ModelForm):
    photo = forms.FileField(widget=AdminImageWidget, label=u'Фотография')

    class Meta:
        model = News