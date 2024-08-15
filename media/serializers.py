from rest_framework import serializers
from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file', 'uploaded_at', 'owner']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url
