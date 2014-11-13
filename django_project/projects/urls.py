# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

from .views import ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectListView, ProjectDeleteView, \
    ProjectApproveView


urlpatterns = patterns("",
    # {% url 'projects:form' %}
    url(
        regex=r"^form/$",
        view=ProjectCreateView.as_view(),
        name="form"
    ),
    # {% url 'projects:detail' pk %}
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=ProjectDetailView.as_view(),
        name="detail"
    ),
    # {% url 'projects:form' pk %}
    url(
        regex=r"^form/(?P<pk>\d+)/$",
        view=ProjectUpdateView.as_view(),
        name="form"
    ),
    # {% url 'projects:list' %}
    url(
        regex=r"^list/$",
        view=ProjectListView.as_view(),
        name="list"
    ),
    # {% url 'projects:list' username %}
    url(
        regex=r"^list/(?P<username>[\w.@+-]+)/$",
        view=ProjectListView.as_view(),
        name="list"
    ),
    # {% url 'projects:delete' pk %}
    url(
        regex=r"^delete/(?P<pk>\d+)/$",
        view=ProjectDeleteView.as_view(),
        name="delete"
    ),
    # {% url 'projects:approve' pk %}
    url(
        regex=r"^approve/(?P<pk>\d+)/$",
        view=ProjectApproveView.as_view(),
        name="approve"
    ),
)