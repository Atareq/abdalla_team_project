from rest_framework.permissions import SAFE_METHODS, BasePermission


class ProductPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PATCH', 'PUT', 'DELETE', 'POST'] and (
             request.user.is_admin):
            return True
        elif request.method in SAFE_METHODS:
            return True
        return False
