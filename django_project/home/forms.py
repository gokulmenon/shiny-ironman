# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):

    name = forms.CharField(_('name'))
    email = forms.EmailField(_('e-mail'))
    phone_no = forms.CharField(_('phone number'))
    title = forms.CharField(_('title'))
    body = forms.CharField(_('body'), widget=forms.Textarea)

    def send_email(self, header=''):
        subject = self.cleaned_data['title']
        body = self.cleaned_data['body']

        if subject and body:
            subject = '%s - %s' % (header, subject)
            ctx_dict = self.cleaned_data


            txt_content = render_to_string('contact/contact_email.txt',
                                       ctx_dict)
            html_content = render_to_string('contact/contact_email.html',
                                       ctx_dict)

            from_email = settings.DEFAULT_FROM_EMAIL
            to = from_email
            try:
                msg = EmailMultiAlternatives(subject, txt_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse_lazy('home:contact', kwargs={'result': 'success'}))
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')


class EstimateForm(forms.Form):

    name = forms.CharField(_('name'))
    email = forms.EmailField(_('e-mail'))
    phone_no = forms.CharField(_('phone number'))
    title = forms.CharField(_('title'))
    body = forms.CharField(_('body'), widget=forms.Textarea)

    def send_email(self, header=''):
        subject = self.cleaned_data['title']
        body = self.cleaned_data['body']

        if subject and body:
            subject = '%s - %s' % (header, subject)
            ctx_dict = self.cleaned_data


            txt_content = render_to_string('contact/contact_email.txt',
                                       ctx_dict)
            html_content = render_to_string('contact/contact_email.html',
                                       ctx_dict)

            from_email = settings.DEFAULT_FROM_EMAIL
            to = from_email
            try:
                msg = EmailMultiAlternatives(subject, txt_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse_lazy('home:contact', kwargs={'result': 'success'}))
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')