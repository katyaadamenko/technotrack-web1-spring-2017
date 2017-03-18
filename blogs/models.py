#coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'

    def __unicode__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey('blogs.Blog', related_name='posts', default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-created_at', )

    def __unicode__(self):
        return "{} от {}".format(self.title, self.created_at)