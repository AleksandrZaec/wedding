from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class UserManager(BaseUserManager):
    def create_user(self, phone, first_name, last_name, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(phone)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    phone = PhoneNumberField(verbose_name='Телефон', unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_presence = models.BooleanField(verbose_name='Присутствие')
    is_organizers = models.BooleanField(default=False, verbose_name='Организатор', **NULLABLE)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return str(self.phone)
