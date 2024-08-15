from rest_framework import serializers
from .models import Poster


class PosterSerializer(serializers.ModelSerializer):
    event_time = serializers.TimeField(format='%H:%M', input_formats=['%H:%M'])
    event_day = serializers.CharField()

    class Meta:
        model = Poster
        fields = ['event_name', 'event_time', 'event_day', 'event_location', "id"]
