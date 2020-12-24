from rest_framework.permissions import BasePermission


class IsRector(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated or not user.is_active:
            return False

        if user.role == 'r':
            return True
        return False


class IsHeadOfDep(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or not user.is_active:
            return False
        if user.role == 'hod':
            return True
        return False
