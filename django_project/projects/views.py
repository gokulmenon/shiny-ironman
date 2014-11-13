# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, RedirectView
from django.views.generic.detail import SingleObjectMixin

from braces.views import LoginRequiredMixin

from core.views import OwnerPermissionMixin

from .forms import ProjectModelForm
from .models import Project


class ProjectPageMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ProjectPageMixin, self).get_context_data(**kwargs)

        context['project_page'] = True

        return context


class ProjectCreateView(LoginRequiredMixin, ProjectPageMixin, CreateView):

    model = Project
    form_class = ProjectModelForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()

        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(OwnerPermissionMixin, ProjectPageMixin, UpdateView):

    model = Project
    form_class = ProjectModelForm


class ProjectDetailView(ProjectPageMixin, DetailView):
    
    model = Project


class ProjectListView(ProjectPageMixin, ListView):

    model = Project
    queryset = Project.objects.filter(deleted=False)
    paginate_by = 20

    def get_queryset(self):
        """
        Get the list of items for this view. This must be an iterable, and may
        be a queryset (in which qs-specific behavior will be enabled).
        """
        user = self.request.user

        queryset = super(ProjectListView, self).get_queryset()

        order_by = self.request.GET.get('order_by', None)

        if order_by=='price':
            queryset = queryset.order_by('-estimated_price')
        else:
            queryset = queryset.order_by('-deadline')

        username = self.kwargs.get('username', '')
        if username:
            queryset = queryset.filter(owner__username=username)

        if not user.is_staff:
            if not user.is_authenticated() or (user.is_authenticated() and user.username != username):
                queryset = queryset.filter(inspected=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)

        context['order_by'] = self.kwargs.get('order_by', '')
        context['username'] = self.kwargs.get('username', '')
        return context


class ProjectDeleteView(OwnerPermissionMixin, ProjectPageMixin, DeleteView):

    model = Project
    success_url = reverse_lazy('projects:list')


class ProjectApproveView(SingleObjectMixin, RedirectView):

    model = Project

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            project = self.get_object()
            if project.inspected:
                project.inspected = True
            else:
                project.inspected = False
            project.save()

        return super(ProjectApproveView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return reverse_lazy('projects:detail', kwargs={'pk': self.get_object().pk})