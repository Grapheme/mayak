# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin

from yugregion.shanson_advertisers.models import Managers, Shanson_Action, Research, Partners

class ManagersAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Фамилия Имя:'), {'fields': ['is_published', ('name', 'surname', ), 'post', 'photo', 'text', 'phone', 'email', 'weight', ]}),
    )
    list_display = ('__unicode__', 'post', 'is_published', 'weight', )
    list_editable = ('is_published', 'weight', )
    list_filter = ('post', )
    search_fields = ('surname', 'name', 'text', )

class Shanson_ActionAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_s'
    fieldsets = (
        (None, {'fields': [('is_published', 'weight', ), 'title', 'date_s', 'date_e', 'anons', 'description', 'gallery', ]}),
    )
    list_display = ('__unicode__', 'is_published', 'weight', )
    list_editable = ('is_published', 'weight', )
    list_filter = ('is_published', )
    search_fields = ('title', 'anons', 'description', )

class ResearchAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['is_published', 'title', 'embed_code', ]}),
    )
    list_display = ('__unicode__', 'is_published', 'embed_code', )
    list_editable = ('is_published', 'embed_code', )
    list_filter = ('is_published', )
    search_fields = ('title', )

class PartnersAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': [('is_published', 'weight', ), 'title', 'logo', ]}),
    )
    list_display = ('__unicode__', 'title', 'logo', 'logo_thumb', 'weight', 'is_published', )
    list_editable = ('title', 'logo', 'is_published', 'weight', )
    list_filter = ('is_published', )
    search_fields = ('title', )

admin.site.register(Research, ResearchAdmin)
admin.site.register(Shanson_Action, Shanson_ActionAdmin)
admin.site.register(Managers, ManagersAdmin)
admin.site.register(Partners, PartnersAdmin)