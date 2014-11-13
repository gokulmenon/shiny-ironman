# -*- coding: utf-8 -*-
from haystack import indexes

from .models import User


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')
    username = indexes.CharField(model_attr='username')

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(is_active=True).order_by('username')