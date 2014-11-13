# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Application


class ApplicationModelForm(forms.ModelForm):
    estimated_price = forms.CharField(label=_("Estimated Price (10,000 KRW)"))

    class Meta():
        model = Application
        fields = ['description', 'estimated_price', 'estimated_days']