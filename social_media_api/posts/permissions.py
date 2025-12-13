from rest_framework.permissions import BasePermission, SAFE_METHODS

# Allow read-only access to anyone.
# Allow write access only to the object owner.

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
