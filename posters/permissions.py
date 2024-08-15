from rest_framework import permissions


class IsSuperuserOrIsOrganizer(permissions.BasePermission):
    """
    Разрешить создание, изменение и удаление постеров только суперпользователям и пользователям с флагом is_organizers=True.
    Разрешить просмотр постеров всем пользователям, включая неавторизованных.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
                request.user and
                request.user.is_authenticated and
                (request.user.is_superuser or request.user.is_organizers)
        )
