from rest_framework import serializers
from pokemonTeams.models import Box, Pokemon


class BoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = '__all__'