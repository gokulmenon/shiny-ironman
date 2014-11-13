# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import RedirectView, TemplateView

from .views import ContactFormView, EstimateFormView, ProjectManagementFormView


urlpatterns = patterns("",
    url(r'^robots\.txt$',
        TemplateView.as_view(template_name='robots.txt'),
        name='robots.txt'),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    # {% url "home:start" %}
    url(
        regex=r'^start$',
        view=TemplateView.as_view(template_name='start.html'),
        name="start",
    ),
    # {% url "home:home" %}
    url(
        regex=r'^$',
        view=TemplateView.as_view(template_name='home.html'),
        name="home",
    ),
    # {% url "home:404" %}
    url(
        regex=r"^404/$",
        view=TemplateView.as_view(template_name='404.html'),
        name="404",
    ),
    # {% url "home:500" %}
    url(
        regex=r"^500/$",
        view=TemplateView.as_view(template_name='500.html'),
        name="500",
    ),
    # {% url "home:about" %}
    url(
        regex=r"^about/$",
        view=TemplateView.as_view(template_name='about.html'),
        name="about",
    ),
    # {% url "home:privacy" %}
    url(
        regex=r"^privacy/$",
        view=TemplateView.as_view(template_name='privacy.html'),
        name="privacy",
    ),
    # {% url "home:terms" %}
    url(
        regex=r"^terms/$",
        view=TemplateView.as_view(template_name='terms.html'),
        name="terms",
    ),
    # {% url "home:recruit" %}
    url(
        regex=r"^recruit/$",
        view=TemplateView.as_view(template_name='recruit.html'),
        name="recruit",
    ),
    # {% url 'home:form' %}
    url(
        regex=r"^contact/$",
        view=ContactFormView.as_view(),
        name="contact"
    ),
    # {% url 'home:form' result %}
    url(
        regex=r"^contact/(?P<result>\w+)/$",
        view=ContactFormView.as_view(),
        name="contact"
    ),
    # {% url 'home:estimate' %}
    url(
        regex=r"^estimate/$",
        view=EstimateFormView.as_view(),
        name="estimate"
    ),
    # {% url 'home:form' result %}
    url(
        regex=r"^estimate/(?P<result>\w+)/$",
        view=EstimateFormView.as_view(),
        name="estimate"
    ),
    # {% url 'home:project_management' %}
    url(
        regex=r"^project_management/$",
        view=ProjectManagementFormView.as_view(),
        name="project_management"
    ),
    # {% url 'home:project_management' result %}
    url(
        regex=r"^project_management/(?P<result>\w+)/$",
        view=ProjectManagementFormView.as_view(),
        name="project_management"
    ),
)