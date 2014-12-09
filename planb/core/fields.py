# -*- coding: utf-8 -*-

from django.forms.fields import CharField as ChFild, EmailField as EmlFild

class CharField(ChFild):
    def __init__(self, placeholder='', *args, **kwargs):
        self.placeholder = placeholder
        super(CharField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(CharField, self).widget_attrs(widget)
        if self.placeholder is not '':
            attrs.update({u'placeholder': self.placeholder})
        return attrs

class EmailField(EmlFild):
    def __init__(self, placeholder='', *args, **kwargs):
        self.placeholder = placeholder
        super(EmailField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(EmailField, self).widget_attrs(widget)
        if self.placeholder is not '':
            attrs.update({u'placeholder': self.placeholder})
        return attrs