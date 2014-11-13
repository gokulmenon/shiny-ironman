# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from core.models import ConservativeDeleteModel


class Project(TimeStampedModel, ConservativeDeleteModel):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(_('title'), max_length=150)
    description = models.TextField(_('description'))
    location = models.CharField(_('location'), max_length=50)
    estimated_price = models.PositiveIntegerField(_('estimated price'))
    estimated_period = models.PositiveSmallIntegerField(_('estimated period in days'))
    deadline = models.DateField(_('deadline'), null=True, blank=True)
    inspected = models.BooleanField(_('inspected'))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"pk": self.pk})

    def over_deadline(self):
        return self.deadline < date.today()

    def application_list(self):
        from applications.models import Application
        return Application.objects.filter(project=self, deleted=False)