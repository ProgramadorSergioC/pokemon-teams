from rest_framework import permissions

class IsTrainerOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite la acción solo si el usuario es el dueño del entrenador asociado
        return obj.trainer.user == request.user