from django.contrib import admin
from .models import PokemonType, Pokemon, Box, Team, TrainerPokemon

admin.site.register(PokemonType)
admin.site.register(Pokemon)
admin.site.register(Box)
admin.site.register(Team)
admin.site.register(TrainerPokemon)