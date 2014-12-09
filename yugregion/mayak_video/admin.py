# -*- coding: utf-8 -*-

from django.contrib import admin

from yugregion.mayak_video.models import Video


class VideoAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'program', 'date', 'is_published', )
    list_editable = ('is_published', )
    list_filter = ('program', 'is_published', )
    search_fields = ('title', 'text')

admin.site.register(Video, VideoAdmin)
