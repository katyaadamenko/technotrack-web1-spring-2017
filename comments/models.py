#coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Comment(models.Model):
    post = models.ForeignKey('blogs.Post', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = ('created_at', )

    def __unicode__(self):
        return self.author.username
