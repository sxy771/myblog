# notice/models.py

import os
from django.conf import settings
from django.db import models

class Notice(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Writer')
    title = models.CharField(max_length=128, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    hits = models.PositiveIntegerField(verbose_name='views', default=0)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='Pub_date')
    top_fixed = models.BooleanField(verbose_name='Top_fixed', default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Notice'
        verbose_name = 'Notice'
        verbose_name_plural = 'Notice'