from django.db import models

from apps.common.models import BaseModel


class Username(BaseModel):
    username = models.CharField(max_length=250)

    def __str__(self):
        return self.username
