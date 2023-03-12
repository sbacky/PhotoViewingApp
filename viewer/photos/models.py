# viewer/photos/models.py

import datetime
import logging

from django.db import models
from django.utils import timezone

# Get instance of logger using namespace
logger = logging.getLogger(__name__)

class Photo(models.Model):
    name = models.CharField(
        max_length=25,
    )

    taken_date = models.DateField(
        blank=True,
    )

    pub_date = models.DateField(
        auto_now_add=True,
    )

    description = models.TextField(
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
