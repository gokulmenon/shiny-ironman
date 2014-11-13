# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "deleted")

admin.site.register(Portfolio, PortfolioAdmin)