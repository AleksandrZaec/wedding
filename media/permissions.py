# from rest_framework.permissions import BasePermission
#
#
# class IsAuthenticatedOrReadOnly(BasePermission):
#     """
#     Разрешает доступ к методам безопасного чтения всем пользователям,
#     но только авторизованным пользователям разрешает небезопасные методы.
#     """
#
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         return request.user and request.user.is_authenticated
