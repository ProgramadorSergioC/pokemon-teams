from rest_framework import viewsets, status
from pokemonTeams.models import Box
from pokemonTeams.serializers import BoxSerializer
from rest_framework.response import Response


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer



