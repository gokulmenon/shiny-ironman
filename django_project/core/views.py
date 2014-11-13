# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import PermissionDenied

from braces.views import LoginRequiredMixin


class OwnerPermissionMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        object = super(OwnerPermissionMixin, self).get_object()
        user = request.user

        if object.owner != user and not user.is_staff:
            raise PermissionDenied

        return super(OwnerPermissionMixin, self).dispatch(
            request, *args, **kwargs)