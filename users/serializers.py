from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from phonenumber_field.phonenumber import PhoneNumber
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_presence = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'is_presence']

    def validate_phone(self, value):
        try:
            phone_number = PhoneNumber.from_string(value, region='RU')
            normalized_phone = phone_number.as_e164
        except Exception:
            raise ValidationError("Неверный формат номера телефона.")
        return normalized_phone

    def validate(self, data):
        if User.objects.filter(phone=data['phone']).exists():
            raise ValidationError("Пользователь с таким номером телефона уже существует.")
        return data

    def create(self, validated_data):

        phone = validated_data['phone']
        user = User.objects.create_user(
            phone=phone,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_presence=validated_data['is_presence']
        )
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'is_presence']
