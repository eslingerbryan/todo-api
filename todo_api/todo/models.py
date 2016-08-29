from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
