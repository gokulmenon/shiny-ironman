# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

from .views import ApplicationCreateView, ApplicationDetailView, ApplicationUpdateView, ApplicationListview, ApplicationDeleteView


urlpatterns = patterns("",
    # {% url 'applications:form' project_id %}
    url(
        regex=r"^form/(?P<project_id>\d+)/$",
        view=ApplicationCreateView.as_view(),
        name="form"
    ),
    # {% url 'applications:detail' pk %}
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=ApplicationDetailView.as_view(),
        name="detail"
    ),
    # {% url 'applications:form' project_id pk %}
    url(
        regex=r"^form/(?P<project_id>\d+)/(?P<pk>\d+)/$",
        view=ApplicationUpdateView.as_view(),
        name="form"
    ),
    # {% url 'applications:list' %}
    url(
        regex=r"^list/$",
        view=ApplicationListview.as_view(),
        name="list"
    ),
    # {% url 'applications:list' project_id %}
    url(
        regex=r"^list/(?P<project_id>\d+)/$",
        view=ApplicationListview.as_view(),
        name="list"
    ),
    # {% url 'applications:delete' pk %}
    url(
        regex=r"^delete/(?P<pk>\d+)/$",
        view=ApplicationDeleteView.as_view(),
        name="delete"
    ),
)