# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView

from braces.views import LoginRequiredMixin

from core.views import OwnerPermissionMixin

from .forms import PortfolioModelForm
from .models import Portfolio


class PortfolioPageMixin(object):
    """ Add 'portfolio_page' variable as 'True' in the context
    """

    def get_context_data(self, **kwargs):
        context = super(PortfolioPageMixin, self).get_context_data(**kwargs)

        context['portfolio_page'] = True

        return context


class PortfolioCreateView(LoginRequiredMixin, PortfolioPageMixin, CreateView):

    model = Portfolio
    form_class = PortfolioModelForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()

        return super(PortfolioCreateView, self).form_valid(form)


class PortfolioDetailView(PortfolioPageMixin, DetailView):
    
    model = Portfolio


class PortfolioUpdate(OwnerPermissionMixin, PortfolioPageMixin, UpdateView):

    model = Portfolio
    form_class = PortfolioModelForm


class PortfolioListView(PortfolioPageMixin, ListView):

    model = Portfolio
    queryset = Portfolio.objects.filter(deleted=False).order_by('-created')
    paginate_by = 20

    def get_queryset(self):
        queryset = super(PortfolioListView, self).get_queryset()

        username = self.kwargs.get('username', '')
        if username:
            queryset = queryset.filter(owner__username=username)

        keyword = self.request.GET.get('keyword', None)
        if keyword:
            queryset = queryset.filter(
                Q(owner__username=keyword) | Q(title__icontains=keyword) | Q(description__icontains=keyword)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PortfolioListView, self).get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username', '')
        context['keyword'] = self.request.GET.get('keyword', '')
        return context


class PortfolioDeleteView(OwnerPermissionMixin, PortfolioPageMixin, DeleteView):

    model = Portfolio
    success_url = reverse_lazy('portfolios:list')