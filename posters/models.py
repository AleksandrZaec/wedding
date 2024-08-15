from django.db import models
from django.utils import timezone
from users.models import NULLABLE
from django.db import models


class Poster(models.Model):
    event_name = models.CharField(max_length=255, verbose_name='Имя события')
    event_time = models.TimeField(verbose_name='Время события')
    event_day = models.CharField(max_length=50, verbose_name='День события')
    event_location = models.CharField(max_length=255, verbose_name='Место события', **NULLABLE)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'Постер события'
        verbose_name_plural = 'Постеры событий'
        ordering = ['event_time']

