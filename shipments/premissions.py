from rest_framework.permissions import BasePermission


class ShipmentsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PATCH', 'PUT', 'DELETE', 'GET'] and (
             request.user.is_admin):
            return True
        return False


class ShipmentsUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST'] and not request.user.is_admin:
            return True
        return False
