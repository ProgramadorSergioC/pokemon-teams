from rest_framework import serializers
from pokemonTeams.models import TrainerPokemon, Box
from django.db.models import F, Count



class TrainerPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerPokemon
        fields = ['id', 'pokemon', 'trainer', 'level', 'box', 'team']

    def create(self, validated_data):
        # Get the trainer from validated_data
        trainer = validated_data['trainer']

        # If no box is specified, assign the first box associated with the trainer
        if 'box' not in validated_data or validated_data['box'] is None:
            # If no available boxes are found, filter to get the first box with space available for more Pokémon
            validated_data['box'] = trainer.box_set.annotate(num_pokemon=Count('trainerpokemon')).filter(
                space_limit__gt=F('num_pokemon')).first()

        # If no available boxes are found, raise an error
        if validated_data['box'] is None:
            raise serializers.ValidationError("No available box with sufficient space for capturing more Pokémon.")

        # Create the TrainerPokemon instance
        trainer_pokemon = TrainerPokemon.objects.create(**validated_data)

        return trainer_pokemon
