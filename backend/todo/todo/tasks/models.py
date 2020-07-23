from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Task(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="title"
    )
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title[:15]
