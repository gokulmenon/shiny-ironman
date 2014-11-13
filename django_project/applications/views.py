# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.views import reverse
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView

from braces.views import LoginRequiredMixin

from core.views import OwnerPermissionMixin
from projects.models import Project

from .forms import ApplicationModelForm
from .models import Application


class ApplicationPageMixin(object):
    """ Add 'portfolio_page' variable as 'True' in the context
    """

    def get_context_data(self, **kwargs):
        context = super(ApplicationPageMixin, self).get_context_data(**kwargs)

        context['application_page'] = True

        return context


class ProjectOpenRequiredMixin(object):
    """
    View mixin which verifies that the user is authenticated.

    NOTE:
        This should be the left-most mixin of a view, except when
        combined with CsrfExemptMixin - which in that case should
        be the left-most mixin.
    """
    def dispatch(self, request, *args, **kwargs):
        project = self.get_project()

        if project.over_deadline():
            return redirect(reverse('projects:list'))
        return super(ProjectOpenRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class OwnerApplicantPermissionMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        object = super(OwnerApplicantPermissionMixin, self).get_object()
        user = request.user

        if object.owner != user and object.project.owner != user and not user.is_staff:
            raise PermissionDenied

        return super(OwnerApplicantPermissionMixin, self).dispatch(
            request, *args, **kwargs)


class ApplicationProjectMixin(object):

    def get_project(self):
        project_id = self.kwargs.get('project_id', None)
        if project_id:
            return get_object_or_404(Project, pk=project_id)
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super(ApplicationProjectMixin, self).get_context_data(**kwargs)
        context['project'] = self.get_project()
        return context


class ApplicationCreateView(LoginRequiredMixin, ApplicationProjectMixin, ProjectOpenRequiredMixin, CreateView):

    model = Application
    form_class = ApplicationModelForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.project = self.get_project()
        self.object = form.save()

        return super(ApplicationCreateView, self).form_valid(form)


class ApplicationDetailView(OwnerApplicantPermissionMixin, DetailView):
    
    model = Application


class ApplicationUpdateView(OwnerPermissionMixin, ApplicationProjectMixin, ProjectOpenRequiredMixin, UpdateView):

    model = Application
    form_class = ApplicationModelForm


class ApplicationListview(LoginRequiredMixin, ApplicationPageMixin, ApplicationProjectMixin, ListView):

    model = Application
    queryset = Application.objects.filter(deleted=False).order_by('-created')
    paginate_by = 20

    def get_queryset(self):
        queryset = super(ApplicationListview, self).get_queryset()
        project_id = self.kwargs.get('project_id', None)
        if project_id:
            queryset = queryset.filter(project__pk=project_id)
        elif not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ApplicationDeleteView(OwnerPermissionMixin, ApplicationPageMixin, DeleteView):

    model = Application
    success_url = reverse_lazy('applications:list')