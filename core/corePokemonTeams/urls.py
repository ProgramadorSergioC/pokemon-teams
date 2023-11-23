"""Core-corePokemonTeams URL Configuration

The `urlpatterns` list routes URLs to pokemon. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function pokemon
    1. Add an import:  from my_app import pokemon
    2. Add a URL to urlpatterns:  path('', pokemon.home, name='home')
Class-based pokemon
    1. Add an import:  from other_app.pokemon import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pokemonTeams.urls')),
    path('api/', include('accounts.urls')),
]
