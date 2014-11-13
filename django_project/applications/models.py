# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from core.models import ConservativeDeleteModel
from projects.models import Project


class Application(TimeStampedModel, ConservativeDeleteModel):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project)
    description = models.TextField(_('description'))
    estimated_price = models.PositiveIntegerField(_('estimated price'))
    estimated_days = models.PositiveSmallIntegerField(_('estimated days'))

    unique_together = (("owner", "project"),)

    def __unicode__(self):
        return 'application of %s for %s' % (self.owner, self.project.title)

    def save(self, *args, **kwargs):
        if not self.pk:
            default_protocol = getattr(settings, 'DEFAULT_HTTP_PROTOCOL', 'http')
            site_name = Site.objects.get_current().name
            site_domain = Site.objects.get_current().domain
            project_title = self.project.title
            application_url = reverse('applications:list', kwargs={'project_id': self.project.pk})
            subject = render_to_string('applications/mail/new_application_subject.txt', {
                    'site_name': site_name,
                    'project_title': project_title,
                })
            txt_message = render_to_string('applications/mail/new_application_body.txt', {
                    'site_name': site_name,
                    'site_url': '%s://%s' % (default_protocol, site_domain),
                    'project_title': project_title,
                    'applicant_name': self.owner.username,
                    'application_url': application_url,
                })

            try:
                send_mail(subject, txt_message, settings.DEFAULT_FROM_EMAIL,
                    [self.project.owner.email,])
            except Exception as e:
                #print e
                pass #fail silently

        super(Application, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("applications:detail", kwargs={"pk": self.pk})

    def over_deadline(self):
        return self.project.over_deadline()

