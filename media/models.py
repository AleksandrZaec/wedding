from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Media(models.Model):
    """
    Модель медиафайлов (фото и видео), загружаемых пользователями.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Отправитель')
    file = models.FileField(upload_to='media/', verbose_name='Медиафайл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Время загрузки')

    class Meta:
        verbose_name = 'Медиафайл'
        verbose_name_plural = 'Медиафайлы'
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.file.name}"
