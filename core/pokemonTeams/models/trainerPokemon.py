from django.db import models
from . import Pokemon, Box, Team
from accounts.models import Trainer


class TrainerPokemon(models.Model):
    DEFAULT_LEVEL = 1
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, null=False, default=DEFAULT_LEVEL)
    box = models.ForeignKey(Box, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon.name} of {self.trainer.user.username} at level {self.level}"
