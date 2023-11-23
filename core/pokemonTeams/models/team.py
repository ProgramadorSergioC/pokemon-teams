from django.db import models
from django.core.exceptions import ValidationError
from . import Pokemon
from accounts.models import Trainer


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pokemons = models.ManyToManyField(Pokemon)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def clean(self):
        # Check if there are more than 6 Pokémon in the team
        if self.pokemons.count() > 6:
            raise ValidationError("A team cannot have more than 6 Pokémon.")