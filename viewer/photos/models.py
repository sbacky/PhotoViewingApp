# viewer/photos/models.py

import datetime
import logging

from django.db import models
from django.utils import timezone
from django.db.models import CharField, DateField, TextField

# Get instance of logger using namespace
logger = logging.getLogger(__name__)

class Photo(models.Model):
    name: CharField = models.CharField(
        max_length=25,
    )

    taken_date: DateField = models.DateField(
        blank=True,
    )

    pub_date: DateField = models.DateField(
        auto_now_add=True,
    )

    description: TextField = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        blank=True,
        upload_to="static/images"
    )

    def __repr__(self) -> str:
        return f'{super().__class__()}: {self.name}'
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def was_published_recently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
