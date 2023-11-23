from rest_framework import viewsets
from pokemonTeams.models import Team
from pokemonTeams.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer