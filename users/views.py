from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .permissions import IsOrganizerOrSuperuser
from .serializers import UserCreateSerializer, UserListSerializer
from rest_framework import status
from rest_framework.response import Response


class UserCreateAPIView(CreateAPIView):
    """
    Эндпоинт для создания пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Вы в списке гостей!'}, status=status.HTTP_201_CREATED, headers=headers)


class UserListAPIView(ListAPIView):
    """
    Эндпоинт для получения списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsOrganizerOrSuperuser]