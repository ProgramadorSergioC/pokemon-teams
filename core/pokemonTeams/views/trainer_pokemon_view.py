from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F, Count
from pokemonTeams.models import TrainerPokemon, Team, Box
from pokemonTeams.serializers import TrainerPokemonSerializer
from pokemonTeams.permissions import IsTrainerOwner


class TrainerPokemonViewSet(viewsets.ModelViewSet):
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsTrainerOwner]

    @action(detail=False, methods=['post'])
    def add_to_team(self, request, trainerpokemon_id, team_id):
        try:
            trainer_pokemon = TrainerPokemon.objects.get(id=trainerpokemon_id)
            team = Team.objects.get(id=team_id, trainer=trainer_pokemon.trainer)
        except TrainerPokemon.DoesNotExist:
            return Response({'error': 'TrainerPokemon not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Team.DoesNotExist:
            return Response({'error': 'Team not found or does not belong to the trainer.'},
                            status=status.HTTP_404_NOT_FOUND)

        # Check if the team already has 6 Pokémon
        print("hol adrian")
        print(team.trainerpokemon_set.all())
        print(team.trainerpokemon_set.count())
        if team.trainerpokemon_set.count() >= 6:
            return Response({'error': 'The team already has 6 Pokémon. Cannot add more.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Remove TrainerPokemon from the associated box
        trainer_pokemon.box = None
        trainer_pokemon.save()

        # Set TrainerPokemon to the specified team
        trainer_pokemon.team = team
        trainer_pokemon.save()

        serializer = TrainerPokemonSerializer(trainer_pokemon)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def add_to_box(self, request, trainerpokemon_id, box_id=None):
        try:
            trainer_pokemon = TrainerPokemon.objects.get(id=trainerpokemon_id)
        except TrainerPokemon.DoesNotExist:
            return Response({'error': 'TrainerPokemon not found.'}, status=status.HTTP_404_NOT_FOUND)

        if box_id:
            try:
                box = Box.objects.get(id=box_id, trainer=trainer_pokemon.trainer)
            except Box.DoesNotExist:
                return Response({'error': 'Box not found or does not belong to the trainer.'},
                                status=status.HTTP_404_NOT_FOUND)

            # Check if the team already has the space limit Pokémon
            if box.trainerpokemon_set.count() >= box.space_limit:
                return Response({'error': 'The box already has reach the Pokémon space limit. Cannot add more.'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:

            box = trainer_pokemon.trainer.box_set.annotate(num_pokemon=Count('trainerpokemon')).filter(
                space_limit__gt=F('num_pokemon')).first()

            # If no available boxes are found, raise an error
            if box is None:
                return Response({'error': 'No available box with sufficient space for capturing more Pokémon.'},
                                status=status.HTTP_400_BAD_REQUEST)

        # Remove TrainerPokemon from the associated team if has one
        if trainer_pokemon.team:
            trainer_pokemon.team = None
            trainer_pokemon.save()

        # Set TrainerPokemon to the specified team
        trainer_pokemon.box = box
        trainer_pokemon.save()

        serializer = TrainerPokemonSerializer(trainer_pokemon)
        return Response(serializer.data, status=status.HTTP_200_OK)
