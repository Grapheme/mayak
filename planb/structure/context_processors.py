# -*- coding: utf-8 -*-

from django.conf import settings

from planb.structure.models import StructureNode

def site_name(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'YANDEX_KEY': settings.YANDEX_KEY
    }

def current_node(request):
    current_root_node = current_top_node = current_node = StructureNode.objects.get_by_path(request.path)
    if current_node and current_node.get_ancestors().filter(level=2).count() > 0:
        current_root_node = current_node.get_ancestors().filter(level=2)[0]
    if current_node and current_node.get_ancestors().filter(level=3).count() > 0:
        current_top_node = current_node.get_ancestors().filter(level=3)[0]
    return {
        'current_node': current_node,
        'current_root_node': current_root_node,
        'current_top_node': current_top_node
    }

def breadcrumbs(request):
    current_path = request.path[1:]
    if current_path.endswith('/'):
        current_path = current_path[:-1]
    crumbs = current_path.split('/')[:-1]
    result = list()
    for i, j in enumerate(crumbs):
        path = '/%s/' %('/'.join(crumbs[:i+1]))
        if StructureNode.objects.published(path=path).exists():
            result.append(StructureNode.objects.published(path=path)[0])

    return dict(
        breadcrumbs = result,
    )

#EOF