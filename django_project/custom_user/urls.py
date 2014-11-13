# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

from .views import UserDetailView, UserUpdateView


urlpatterns = patterns("",
    # {% url 'users:detail' username %}
    url(
        regex=r"^(?P<username>[\w.@+-]+)/$",
        view=UserDetailView.as_view(),
        name="detail"
    ),
    # {% url 'users:update' username %}
    url(
        regex=r"^update/(?P<username>[\w.@+-]+)/$",
        view=UserUpdateView.as_view(),
        name="update"
    ),
)