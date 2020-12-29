from rest_framework.permissions import BasePermission

from users.models import RoleTypes


class IsRector(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated or not user.is_active:
            return False

        if user.role == RoleTypes.RECTOR:
            return True
        return False


class IsHeadOfDep(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or not user.is_active:
            return False
        if user.role == RoleTypes.HEAD_OF_DEP:
            return True
        return False
