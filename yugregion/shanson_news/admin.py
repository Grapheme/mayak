# -*- coding: utf-8 -*-

from django.contrib import admin

from yugregion.shanson_news.models import News


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'is_published', 'date', )
    list_editable = ('is_published', )
    search_fields = ('title', 'text')


admin.site.register(News, NewsAdmin)