# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "inspected", "deleted")

admin.site.register(Project, ProjectAdmin)