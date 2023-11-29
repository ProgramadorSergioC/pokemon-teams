from django import forms
from .models import PokemonType, Pokemon, Box, Team


class PokemonTypeForm(forms.ModelForm):
    class Meta:
        model = PokemonType
        fields = ['name']


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['pokemon_id', 'name', 'image']

    types = forms.ModelMultipleChoiceField(
        queryset=PokemonType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ['name', 'pokemon', 'space_limit']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'pokemon']