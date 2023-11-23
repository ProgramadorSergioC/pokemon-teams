from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from pokemonTeams.models import TrainerPokemon
from pokemonTeams.serializers import TrainerPokemonSerializer


class TrainerPokemonViewSet(viewsets.ModelViewSet):
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer
    # permission_classes = [IsAuthenticated]