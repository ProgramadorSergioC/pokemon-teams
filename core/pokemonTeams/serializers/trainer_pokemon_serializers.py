from rest_framework import serializers
from pokemonTeams.models import TrainerPokemon


class TrainerPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerPokemon
        fields = ['id', 'pokemon', 'trainer', 'level', 'box', 'team']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Comprobación de la cantidad de pokémons en una Box
        if instance.box:
            box_pokemon_count = instance.box.trainerpokemon_set.count()
            representation['box_full'] = box_pokemon_count >= 30
        else:
            representation['box_full'] = False

        # Comprobación de la cantidad de pokémons en un Team
        if instance.team:
            team_pokemon_count = instance.team.trainerpokemon_set.count()
            representation['team_full'] = team_pokemon_count >= 6
        else:
            representation['team_full'] = False

        return representation
