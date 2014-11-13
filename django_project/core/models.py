# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import hashlib

from google.appengine.api import images
from google.appengine.ext import blobstore

from django.conf import settings
from django.core.cache import cache
from django.db import models

def upload_path_handler(instance, filename, prefix=''):
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    hash_key = hashlib.md5(now).hexdigest()

    return "{prefix}{id}/{key}.{filename}"\
        .format(prefix=prefix, id=instance.id, key=hash_key, filename=filename.split(".")[-1])


def gae_image_url(picture):
    """
    Returns dynamic image resizing url using GAE Images API
    """
    if not picture:
        return ''

    key = 'gae_image_url_%s' % picture.name

    try:
        url = cache.get(key)
    except:
        url = None

    if not url:
        blob_key = blobstore.create_gs_key('/gs%s/%s' % (settings.GOOGLE_CLOUD_STORAGE_BUCKET, str(picture)))
        url = images.get_serving_url(blob_key)

        cache.set(key, url)

    return url


class ConservativeDeleteModel(models.Model):
    """
    An abstract base class model that provides deleted field
    for marking model deletion instead of deleting model from database.

    """
    deleted = models.BooleanField()

    class Meta:
        abstract = True

    def delete(self):
        if self.deleted:
            return False
        self.deleted = True
        self.save()
        return True