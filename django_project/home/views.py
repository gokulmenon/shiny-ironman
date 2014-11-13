# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import FormView

from .forms import ContactForm

class ContactFormView(FormView):

    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return form.send_email(header='[General]')

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)

        context['result'] = self.kwargs.get('result', '')
        return context


class EstimateFormView(FormView):

    form_class = ContactForm
    template_name = 'estimate.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return form.send_email(header='[Estimate]')

    def get_context_data(self, **kwargs):
        context = super(EstimateFormView, self).get_context_data(**kwargs)

        context['result'] = self.kwargs.get('result', '')
        context['estimate_page'] = True

        return context


class ProjectManagementFormView(FormView):

    form_class = ContactForm
    template_name = 'project_management.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return form.send_email(header='[PM]')

    def get_context_data(self, **kwargs):
        context = super(ProjectManagementFormView, self).get_context_data(**kwargs)

        context['result'] = self.kwargs.get('result', '')
        context['project_management_page'] = True

        return context