from django.db import models
from django.core.exceptions import ValidationError
from . import PokemonType


class Pokemon(models.Model):
    pokedex_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    types = models.ManyToManyField(PokemonType)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        # Check if the Pokemon has more than 2 Types
        if self.types.count() > 2:
            raise ValidationError("A team cannot have more than 6 Pokémon.")