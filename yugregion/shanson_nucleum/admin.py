# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin

from yugregion.shanson_nucleum.models import Staff, Programs\
    , ProgramsPhoto, ProgramsArchive, ProgramsArchivePhoto, Promo, Press\
    , Listeners, HitParadRevision, HitParadItem

class StaffAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Фамилия Имя:'), {'fields': [('name', 'surname', ), ]}),
        (('Склонение:'), {'fields': [('name_t', 'surname_t', ), ]}),
        (None, {'fields': ['photo', 'photo_min', 'text', 'programs', 'weight', ]}),
    )
    filter_horizontal = ('programs', )
    list_display = ('__unicode__', 'weight', )
    list_editable = ('weight', )
    list_filter = ('programs', )
    search_fields = ('surname', )

class ProgramsPhotoInline(admin.TabularInline):
    model = ProgramsPhoto
    extra = 3

class ProgramsArchiveInline(admin.TabularInline):
    model = ProgramsArchive
    extra = 1

class ProgramsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': [('is_published', 'weight'), 'title', 'display', 'anons', 'description', 'schedule', 'staff', ]}),
    )
    inlines = [ProgramsPhotoInline, ProgramsArchiveInline]
    filter_horizontal = ('staff', )
    list_display = ('title', 'display', 'is_published', 'weight', )
    list_editable = ('display', 'is_published', 'weight', )
    list_filter = ('display', )
    search_fields = ('title', 'description', 'anons', )

class ProgramsArchivePhotoInline(admin.TabularInline):
    model = ProgramsArchivePhoto
    extra = 3

class ProgramsArchiveAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    fieldsets = (
        (None, {'fields': ['is_published', 'program', 'caption', 'date', ('time_s', 'time_e'), 'description', 'soundcloud', ]}),
    )
    inlines = [ProgramsArchivePhotoInline]
    list_display = ('__unicode__', 'program', 'date', 'is_published', )
    list_editable = ('is_published', )
    list_filter = ('program', 'is_published', )
    search_fields = ('description', )

class PromoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': [('is_published', 'weight'), 'title', 'url', 'program', 'photo', ]}),
    )
    list_display = ('title', 'is_published', 'weight', )
    list_editable = ('is_published', 'weight', )
    list_filter = ('is_published', )

class PressAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': [('is_published', 'weight'), 'magazine', 'date', 'headline', 'pdf', ]}),
    )
    list_display = ('__unicode__', 'is_published', 'weight', )
    list_editable = ('is_published', 'weight', )
    list_filter = ('is_published', )


class ListenersAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'is_published', )
    list_editable = ('is_published', )
    list_filter = ('is_published', )

admin.site.register(Press, PressAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Programs, ProgramsAdmin)
admin.site.register(ProgramsArchive, ProgramsArchiveAdmin)
admin.site.register(Listeners, ListenersAdmin)

admin.site.register(HitParadRevision)
admin.site.register(HitParadItem)

if settings.DEBUG:
    admin.site.register(ProgramsPhoto)
    admin.site.register(ProgramsArchivePhoto)