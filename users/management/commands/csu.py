import os
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Команда для создания суперпользователя.
    """
    help = 'Создание суперпользователя'

    def handle(self, *args, **options):
        phone = os.getenv('SUPERUSER_PHONE')
        if not phone:
            self.stdout.write(self.style.ERROR('SUPERUSER_PHONE не задан в переменных окружения'))
            return

        first_name = os.getenv('SUPERUSER_FIRST_NAME', 'Admin')
        last_name = os.getenv('SUPERUSER_LAST_NAME', 'User')
        password = os.getenv('SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write(self.style.ERROR('SUPERUSER_PASSWORD не задан в переменных окружения'))
            return

        user = User.objects.create_user(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_presence=False
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_presence = False
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Суперпользователь создан: {user.phone}'))
