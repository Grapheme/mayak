# -*- coding: utf-8 -*-

from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

from planb.structure import models
from planb.structure.forms import StructureNodeAdminForm


class PromoAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'is_published',]
    list_editable = ['is_published',]

class StructureNodeExtendFieldInline(admin.TabularInline):
    model = models.StructureNodeExtendField

class RightBlockInline(admin.TabularInline):
    model = models.RightBlock

class StructureNodeAdmin(admin.ModelAdmin):
    exclude = ('parent', )
    form = StructureNodeAdminForm
    inlines = [StructureNodeExtendFieldInline, RightBlockInline, ]
    list_display = ['line_with_indent', 'path_for_admin', 'menu_visible', 'is_published',]
    list_editable = ['menu_visible', 'is_published',]

class UploadAdmin(admin.ModelAdmin):
    list_display = ('file_thumb', 'title', 'get_cl_file_link')

admin.site.register(models.StructureNode, StructureNodeAdmin)
admin.site.register(models.Upload, UploadAdmin)
admin.site.register(models.Promo, PromoAdmin)
