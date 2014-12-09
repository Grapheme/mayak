# -*- coding: utf-8 -*-

from django.contrib import admin

from yugregion.mayak_news.models import News


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    fieldsets = (
        (None, {'fields': ['is_published', 'title', ('date', 'time'), 'text', 'photo', ]}),
    )
    list_display = ('title', 'is_published', 'date', )
    list_editable = ('is_published', )
    search_fields = ('title', 'text')

admin.site.register(News, NewsAdmin)
