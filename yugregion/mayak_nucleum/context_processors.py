# -*- coding: utf-8 -*-

from django.conf import settings

from constance import config


def mayak_context(request):
    return {
        'MAYAK_SHOW_VIDEO_BUTTON': config.MAYAK_SHOW_VIDEO_BUTTON,
        'MAYAK_SHOW_CONSULTATION_BUTTON': config.MAYAK_SHOW_CONSULTATION_BUTTON,
    }
