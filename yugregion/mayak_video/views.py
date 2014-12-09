# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from yugregion.mayak_video.models import Video


def program_video_archive(request, pk='loli'):
    if pk != 'loli':
        transfer = get_object_or_404(Video, id=pk)
    elif Video.objects.published().count():
        transfer = Video.objects.published()[0]
    else:
        raise Http404
    return render_to_response("program/mayak_video_archive.html", RequestContext(request, {
        'transfer': transfer,
    }))
