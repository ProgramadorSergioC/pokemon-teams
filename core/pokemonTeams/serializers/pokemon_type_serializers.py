from rest_framework import serializers
from pokemonTeams.models import PokemonType


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = '__all__'
