from rest_framework import routers
from django.urls import path, re_path
from .views import *

router = routers.DefaultRouter()
router.register(r'boxes', BoxViewSet, basename='box')
router.register(r'pokemons', PokemonViewSet, basename='pokemon')
router.register(r'pokemon-types', PokemonTypeViewSet, basename='pokemon-type')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'trainer-pokemons', TrainerPokemonViewSet, basename='trainer-pokemon')

urlpatterns = [
    path('trainer-pokemon/add_to_team/<int:trainerpokemon_id>/<int:team_id>/',
         TrainerPokemonViewSet.as_view({'post': 'add_to_team'}), name='trainer-pokemon-add-to-team'),
    re_path(r'trainer-pokemon/add_to_box/(?P<trainerpokemon_id>\d+)(/(?P<box_id>\d+))?/',
            TrainerPokemonViewSet.as_view({'post': 'add_to_box'}), name='trainer-pokemon-add-to-box'),
]

urlpatterns += router.urls
