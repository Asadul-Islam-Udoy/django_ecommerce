from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsSelfOfAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and(request.user.is_staff or obj == request.user))
class isAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)