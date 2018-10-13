from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owner to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permission are allowed to any request,
        # so we'll always HET, HEAD or OPTIONS requets
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
