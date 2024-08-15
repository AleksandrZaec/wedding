from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Poster
from .permissions import IsSuperuserOrIsOrganizer
from .serializers import PosterSerializer


class PosterViewSet(viewsets.ModelViewSet):
    """
    ViewSet для просмотра и редактирования постеров.
    """
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
    permission_classes = [IsSuperuserOrIsOrganizer]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({"message": "Событие успешно добавлено!"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
