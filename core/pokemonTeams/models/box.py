from django.db import models
from . import Pokemon
from accounts.models import Trainer


class Box(models.Model):
    name = models.CharField(max_length=100)
    space_limit = models.IntegerField(default=30)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
