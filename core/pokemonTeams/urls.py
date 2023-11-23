from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'boxes', BoxViewSet, basename='box')
router.register(r'pokemons', PokemonViewSet, basename='pokemon')
router.register(r'pokemon-types', PokemonTypeViewSet, basename='pokemon-type')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'trainer-pokemons', TrainerPokemonViewSet, basename='trainer-pokemon')

urlpatterns = router.urls
