from rest_framework import viewsets
from pokemonTeams.models import PokemonType
from pokemonTeams.serializers import PokemonTypeSerializer


class PokemonTypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = PokemonTypeSerializer
