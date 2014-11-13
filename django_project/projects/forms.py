# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Project


class ProjectModelForm(forms.ModelForm):
    title = forms.CharField(label=_("Title"))
    location = forms.CharField(label=_("Location"))
    estimated_price = forms.CharField(label=_("Estimated Price (10,000 KRW)"))
    estimated_period = forms.CharField(label=_("Estimated Time (DAYS)"))
    deadline = forms.DateField(label=_("Deadline (YYYY-MM-DD)"))

    class Meta():
        model = Project
        fields = ['title', 'description', 'location', 'estimated_price', 'estimated_period', 'deadline']