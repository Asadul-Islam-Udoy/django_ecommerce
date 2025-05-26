from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsSelfOfAdmin(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only for authenticated users or full access for admin
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user