# -*- coding: utf-8 -*-

import re

from django.conf import settings
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.utils.html import strip_spaces_between_tags

from planb.structure.models import StructureNode

class StripSpacesMiddleware:
    def process_response(self, request, response):
        if response['Content-Type'].startswith('text/html; '):
            response.content = strip_spaces_between_tags(response.content)
        return response

class CurrentNodeMiddleware:
    def process_request(self, request):
        try:
            node = StructureNode.objects.get(path=request.path)
            if node.redirect_url:
                return HttpResponsePermanentRedirect(node.redirect_url)
        except: pass


class CheckSettingsMiddleware:
    def process_request(self, request):
        error, message = False, 'Errors in settings.py:\n\n'
        if not getattr(settings, 'SECRET_KEY', None):
            error = True
            message += ' * SECRET_KEY not set\n'
        if not getattr(settings, 'SITE_NAME', None):
            error = True
            message += ' * SITE_NAME not set\n'
        if error:
            message += '\nRTFM: https://projects.plan-b.ru/trac/wiki/DjangoProjectTemplate'
            return HttpResponse(message, 'text/plain')
        else:
            return None


class RequestSiteMiddleware:
    def process_request(self, request):
        from django.contrib.sites.models import Site

        site = Site.objects.get_current()
        host = request.META['HTTP_HOST']
        try:
            assert site.name == settings.SITE_NAME
            assert site.domain == host
        except AssertionError:
            site.name = settings.SITE_NAME
            site.domain = host
            site.save()
        request.site = site
        return