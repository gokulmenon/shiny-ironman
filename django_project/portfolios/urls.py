# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

from .views import PortfolioCreateView, PortfolioDetailView, PortfolioUpdate, PortfolioListView, PortfolioDeleteView


urlpatterns = patterns("",
    # {% url 'portfolios:form' %}
    url(
        regex=r"^form/$",
        view=PortfolioCreateView.as_view(),
        name="form"
    ),
    # {% url 'portfolios:detail' pk %}
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=PortfolioDetailView.as_view(),
        name="detail"
    ),
    # {% url 'portfolios:form' portfolio.pk %}
    url(
        regex=r"^form/(?P<pk>\d+)/$",
        view=PortfolioUpdate.as_view(),
        name="form"
    ),
    # {% url 'portfolios:list' %}
    url(
        regex=r"^list/$",
        view=PortfolioListView.as_view(),
        name="list"
    ),
    # {% url 'portfolios:list' username %}
    url(
        regex=r"^list/(?P<username>[\w.@+-]+)/$",
        view=PortfolioListView.as_view(),
        name="list"
    ),
    # {% url 'portfolios:delete' portfolio.pk %}
    url(
        regex=r"^delete/(?P<pk>\d+)/$",
        view=PortfolioDeleteView.as_view(),
        name="delete"
    ),
)