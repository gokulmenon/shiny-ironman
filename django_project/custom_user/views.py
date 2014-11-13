# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, UpdateView

from braces.views import LoginRequiredMixin

from .forms import SimpleUserChangeForm
from .models import User


class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    form_class = SimpleUserChangeForm

    def get_success_url(self):
        return reverse_lazy('users:detail', kwargs={'username': self.object.username})