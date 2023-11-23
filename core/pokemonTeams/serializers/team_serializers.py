from rest_framework import serializers
from pokemonTeams.models import Team
from . import PokemonSerializer


class TeamSerializer(serializers.ModelSerializer):
    pokemons = PokemonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
