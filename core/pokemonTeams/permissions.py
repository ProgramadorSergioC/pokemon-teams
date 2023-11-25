from rest_framework import permissions


class IsTrainerOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only allows actions if the user is the owner
        return obj.trainer.user == request.user
