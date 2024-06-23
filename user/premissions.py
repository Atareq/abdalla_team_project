from rest_framework.permissions import BasePermission


class UserListPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'DELETE'] and request.user.is_admin:
            return True
        return False
