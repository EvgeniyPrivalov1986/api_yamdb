from django.conf import settings
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator

from .models import User
from .validators import validate_username


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для User."""
    class Meta:
        model = User
        fields = '__all__'


class ForUserSerializer(serializers.ModelSerializer):
    """Сериализатор для User. Зарезервированное имя использовать нельзя"""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=200,
        required=True,
        validators=[
            validate_username,
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('role', )


class ForAdminSerializer(serializers.ModelSerializer):
    """Сериализатор для Admin. Зарезервированное имя использовать нельзя"""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        max_length=200,
        required=True,
        validators=[
            validate_username,
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )        


class TokenSerializer(serializers.Serializer):
    """Сериализатор для Token. Зарезервированное имя использовать нельзя."""
    username = serializers.CharField(
        max_length=200, 
        required=True,
        validators=[
            validate_username,
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    confirmation_code = serializers.CharField(max_length=200, required=True)
