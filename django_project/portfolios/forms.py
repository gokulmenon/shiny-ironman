# -*- coding: utf-8 -*-
import os

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Portfolio


class PortfolioModelForm(forms.ModelForm):

    image = forms.ImageField

    class Meta():
        model = Portfolio
        fields = ['title', 'description', 'image',]

    def clean_image(self):
        image = self.cleaned_data.get('image',False)
        if image:
            filename = image.name
            ext = os.path.splitext(filename)[1]
            ext = ext.lower()
            if ext not in ['.jpg', '.jpeg', '.gif', '.png', '.bmp']:
                raise forms.ValidationError(_("Not allowed filetype. Please use jpg, jpeg, gif, png, or bmp."))
            if image.size > 1048576:# 1MB = 1024*1024
                raise forms.ValidationError(_("Image file too large ( > 1 MB )"))
        return image