from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Trainer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TrainerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        trainer_data = validated_data.pop('trainer', {})

        # Create a new User with set_password to encrypt the password
        user = User.objects.create(
            username=trainer_data.get('username'),
            email=trainer_data.get('email')
            # Puedes ajustar otros campos del User según tus necesidades
        )
        user.set_password(trainer_data.get('password'))
        user.save()

        # Create the Trainer associated with the User
        trainer = Trainer.objects.create(
            user=user,
            # Puedes ajustar otros campos del Trainer según tus necesidades
        )

        return trainer

    class Meta:
        model = Trainer
        fields = ['id',]