from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mezzanine.core.models import TimeStamped


class Email(TimeStamped):
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body_plain = models.TextField()
    body_without_quotes = models.TextField()
