# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = patterns("",
    # {% url "core:404" %}
    url(
        regex=r"^404/$",
        view=TemplateView.as_view(template_name='404.html'),
        name="404",
    ),
    # {% url "core:500" %}
    url(
        regex=r"^500/$",
        view=TemplateView.as_view(template_name='500.html'),
        name="500",
    ),
    # {% url "core:about" %}
    url(
        regex=r"^about/$",
        view=TemplateView.as_view(template_name='about.html'),
        name="about",
    ),
    # {% url "core:privacy" %}
    url(
        regex=r"^privacy/$",
        view=TemplateView.as_view(template_name='privacy.html'),
        name="privacy",
    ),
    # {% url "core:terms" %}
    url(
        regex=r"^terms/$",
        view=TemplateView.as_view(template_name='terms.html'),
        name="terms",
    ),
    # {% url "core:contact" %}
    url(
        regex=r"^contact/$",
        view=TemplateView.as_view(template_name='contact.html'),
        name="contact",
    ),
)