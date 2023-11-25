# Generated by Django 4.2.6 on 2023-11-25 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemonTeams', '0004_alter_pokemon_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='pokemons',
        ),
        migrations.AlterField(
            model_name='trainerpokemon',
            name='box',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemonTeams.box'),
        ),
        migrations.AlterField(
            model_name='trainerpokemon',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemonTeams.team'),
        ),
    ]
