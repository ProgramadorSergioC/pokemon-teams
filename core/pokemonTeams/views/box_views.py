from rest_framework import viewsets, status
from pokemonTeams.models import Box, Pokemon
from pokemonTeams.serializers import BoxSerializer, PokemonSerializer
from rest_framework.response import Response


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer



