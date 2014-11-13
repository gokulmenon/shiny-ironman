# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import upload_path_handler, gae_image_url


def user_picture_upload_path_handler(instance, filename):
    return "user/picture/" + upload_path_handler(instance, filename)


class User(AbstractUser):

    about = models.CharField(_('about'), max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to=user_picture_upload_path_handler, null=True)

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse_lazy('users:detail', kwargs={'username': self.username})

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def image_url(self):
        """
        Returns dynamic image resizing url using GAE Images API
        Cache url if asked to in the settings.
        """
        return gae_image_url(image=self.image)