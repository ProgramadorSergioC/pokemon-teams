from django.db import migrations, models

def create_user_and_trainer(apps, schema_editor):
    # Create user
    User = apps.get_model('auth', 'User')
    user = User.objects.create_superuser(username='CazadorDeZubats', password='admin')

    # Create trainer associated to user
    Trainer = apps.get_model('accounts', 'Trainer')
    Trainer.objects.create(user=user)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_user_and_trainer),
    ]