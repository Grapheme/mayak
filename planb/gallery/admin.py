# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect

from planb.gallery.models import Gallery, Gallery_Img
from planb.gallery.widgets import MultiFileInput

class Gallery_ImgInline(admin.TabularInline):
    model = Gallery_Img
    extra = 5

class GalleryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['title', 'description', 'weight', ]}),
    )
    inlines = [Gallery_ImgInline]
    list_display = ('title', 'weight', )
    list_editable = ('weight', )
    search_fields = ('description', 'title', )

class Gallery_ImgAdminForm(forms.ModelForm):
 
    class Meta:
        model = Gallery_Img
        widgets = {'img': MultiFileInput}

class Gallery_ImgAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['is_published', ('gallery', 'img', ), 'description', 'weight', ]}),
    )
    form = Gallery_ImgAdminForm
    list_display = ('gallery', 'img', 'weight', 'is_published', )
    list_editable = ('img', 'weight', 'is_published', )
    list_filter = ('gallery', )
    search_fields = ('gallery', )

    def add_view(self, request, *args, **kwargs):
        img_list = request.FILES.getlist('img',[])
        is_valid = Gallery_ImgAdminForm(request.POST, request.FILES).is_valid()
 
        if request.method == 'GET' or len(img_list) <= 1 or not is_valid:
            return super(Gallery_ImgAdmin, self).add_view(request, *args, **kwargs)
        for img in img_list:
            gallery_id = request.POST['gallery']
            try:
                image = Gallery_Img(gallery_id=gallery_id, img=img)
                image.save()
            except Exception, e:
                messages.error(request, smart_str(e)) 

        return redirect('/admin/gallery/gallery_img/')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Gallery_Img, Gallery_ImgAdmin)