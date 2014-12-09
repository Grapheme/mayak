# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from yugregion.mayak_consultation.models import Consiliario, Question,\
    SubjectConsultation


###########
# Filters #
###########

class AnswerFilter(SimpleListFilter):
    title = u'Ответ'
    parameter_name = 'answer'

    def lookups(self, request, model_admin):
        return (
            ('true', u'Имеется ответ'),
            ('false', u'Без Ответа'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.exclude(answer='')
        if self.value() == 'false':
            return queryset.filter(answer='')


#########
# Admin #
#########

class ConsiliarioAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'is_archive', 'is_published', )
    list_editable = ('is_archive', 'is_published', )
    list_filter = ('is_archive', 'is_published', 'subject', )

admin.site.register(Consiliario, ConsiliarioAdmin)


class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('__unicode__', 'email', 'is_published' )
    list_editable = ('is_published', )
    list_filter = ('is_published', AnswerFilter, 'consiliario', 'consiliario__is_archive')

admin.site.register(Question, QuestionAdmin)


class SubjectConsultationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'ordering', )
    list_editable = ('ordering', )

admin.site.register(SubjectConsultation, SubjectConsultationAdmin)
