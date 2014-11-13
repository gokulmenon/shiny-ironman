# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


from core.models import upload_path_handler, gae_image_url, ConservativeDeleteModel


def portfolio_picture_upload_path_handler(instance, filename):
    return "portfolio/picture/" + upload_path_handler(instance, filename)


class Portfolio(TimeStampedModel, ConservativeDeleteModel):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(_('title'), max_length=150)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), upload_to=portfolio_picture_upload_path_handler, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolios:detail", kwargs={"pk": self.pk})

    def image_url(self):
        """
        Returns dynamic image resizing url using GAE Images API
        Cache url if asked to in the settings.
        """
        return gae_image_url(image=self.image)