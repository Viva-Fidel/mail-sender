# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from subscribers.models import Subscriber

import uuid

# Create your models here.
class Report(models.Model):
    email = models.ForeignKey(
        Subscriber, on_delete=models.CASCADE)
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_of_mailing = models.DateTimeField()
    is_opened = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)