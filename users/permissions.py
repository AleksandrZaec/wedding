from rest_framework import permissions


class IsOrganizerOrSuperuser(permissions.BasePermission):
    """
    Доступ разрешён только организаторам (is_organizers=True) и суперпользователям (is_superuser=True).
    Все остальные пользователи не имеют доступа ни к чтению, ни к каким-либо другим действиям.
    """

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and
                (request.user.is_organizers or request.user.is_superuser))
