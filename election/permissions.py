from rest_framework import permissions

class CanCreateOrUpdateElectionPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method.lower() == 'post' or request.method.lower() == 'put':
            if request.user.is_superuser:
                return True
            else:
                return False

        return True
