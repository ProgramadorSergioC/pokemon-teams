from rest_framework import serializers
from pokemonTeams.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

    # def validate_types(self, value):
    #     if value.count() > 2:
    #         raise serializers.ValidationError("Un Pokémon no puede tener más de 2 tipos.")
    #     return value
