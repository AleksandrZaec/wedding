from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Media
from rest_framework.permissions import IsAuthenticated
from .serializers import MediaSerializer
from rest_framework.decorators import action
import mimetypes


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist('files')
        if not files:
            return Response({'error': 'No files provided.'}, status=status.HTTP_400_BAD_REQUEST)

        media_objects = []
        for file in files:
            media = Media.objects.create(
                owner=request.user,
                file=file
            )
            media_objects.append(media)

        serializer = self.get_serializer(media_objects, many=True)
        return Response({"message": "Успешно загружено!"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], url_path='download')
    def download_file(self, request, pk=None):
        media = get_object_or_404(Media, pk=pk)

        content_type, _ = mimetypes.guess_type(media.file.name)
        if content_type is None:
            content_type = 'application/octet-stream'

        response = FileResponse(media.file.open(), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{media.file.name}"'
        return response
