# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("owner", "project", "deleted")

admin.site.register(Application, ApplicationAdmin)