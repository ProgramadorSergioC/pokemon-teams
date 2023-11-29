from django.db import migrations


def insert_pokemon_types(apps, schema_editor):
    PokemonType = apps.get_model('pokemonTeams', 'PokemonType')

    types_first_generation = [
        "Grass", "Fire", "Water", "Electric",
        "Bug", "Normal", "Poison", "Ice",
        "Fighting", "Flying", "Psychic", "Ground",
        "Rock", "Ghost", "Dragon"
    ]

    for type_name in types_first_generation:
        PokemonType.objects.create(name=type_name)


class Migration(migrations.Migration):

    dependencies = [
        ('pokemonTeams', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_pokemon_types),
    ]