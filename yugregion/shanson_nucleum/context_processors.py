# -*- coding: utf-8 -*-

from django.conf import settings

from yugregion.shanson_nucleum.forms import OrderSongForm

def order_song(request):
    if request.path.find('shanson') != -1:
        order_form = OrderSongForm(request.GET or None)
        return {
            'order_form': order_form,
        }
    return {}

#EOF