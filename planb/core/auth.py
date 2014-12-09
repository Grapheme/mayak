# -*- coding: utf-8 -*-

from django.contrib.auth.backends import ModelBackend
from django.contrib.contenttypes.models import ContentType 

__all__ = (
    'CustomModelBackend', 
    'staff_can_add',
    'staff_can_change',
    'staff_can_delete'
)

STAFF_CAN_ADD, STAFF_CAN_CHANGE, STAFF_CAN_DELETE = set(), set(), set()

def staff_can_add(models):
    for model in models:
        STAFF_CAN_ADD.add(model)
def staff_can_change(models):
    for model in models:
        STAFF_CAN_CHANGE.add(model)
def staff_can_delete(models):
    for model in models:
        STAFF_CAN_DELETE.add(model)

class CustomModelBackend(ModelBackend):
    check_perms = ('can_add', 'can_change', 'can_delete')

    def get_all_permissions(self, user_obj):
        if not hasattr(user_obj, '_perm_cache'):
            user_obj._perm_cache = set()
            for ctype in ContentType.objects.all():
                model = ctype.model_class()
                if model in STAFF_CAN_ADD:
                    user_obj._perm_cache.add('%s.add_%s' % (ctype.app_label, ctype.model))
                if model in STAFF_CAN_CHANGE:
                    user_obj._perm_cache.add('%s.change_%s' % (ctype.app_label, ctype.model))
                if model in STAFF_CAN_DELETE:
                    user_obj._perm_cache.add('%s.delete_%s' % (ctype.app_label, ctype.model))
        return user_obj._perm_cache