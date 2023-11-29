from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .models import Trainer
from .serializers import UserSerializer, TrainerSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Llama al método save del serializer con los datos de la solicitud
        serializer.save(trainer=self.request.data.get('trainer', {}))

    # def perform_create(self, serializer):
    #     # Extract data from the request for Trainer creation
    #     trainer_data = self.request.data.get('trainer', {})
    #     print(trainer_data)
    #     # Create a new User with set_password to encrypt the password
    #     user = User.objects.create(
    #         username=trainer_data.get('username'),
    #         email=trainer_data.get('email')
    #         # You can adjust other User fields according to your needs
    #     )
    #     print(user)
    #     user.set_password(trainer_data.get('password'))
    #     user.save()
    #
    #     # Create the Trainer associated with the User
    #     trainer = Trainer.objects.create(
    #         user=user,
    #         # You can adjust other Trainer fields according to your needs
    #     )
    #     print(trainer)
    #     # Call the create method of the serializer with the new Trainer
    #     serializer.create(validated_data=trainer_data)

    def perform_update(self, serializer):
        # Extract data from the request for Trainer update
        trainer_data = self.request.data.get('trainer', {})

        # Get the User associated with the Trainer
        user = serializer.instance.user

        # Update User fields based on the request data
        user.username = trainer_data.get('username', user.username)
        user.email = trainer_data.get('email', user.email)

        # Use set_password to securely set the new password
        new_password = trainer_data.get('password')
        if new_password:
            user.set_password(new_password)

        # You can adjust other User fields according to your needs

        # Save changes to the User
        user.save()

        # Call the update method of the serializer with the updated Trainer
        serializer.update(serializer.instance, trainer_data)

    def perform_destroy(self, instance):
        # Delete the User associated with the Trainer
        instance.user.delete()

        # Call the destroy method of the serializer with the Trainer to delete
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
