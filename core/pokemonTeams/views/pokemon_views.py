from rest_framework import viewsets
from pokemonTeams.models import Pokemon
from pokemonTeams.serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            # Registra información detallada sobre la excepción
            print(f"Error al crear un Pokémon: {e}")
            raise