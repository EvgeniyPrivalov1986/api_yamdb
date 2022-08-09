from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from .validators import validate_username

MAX_LENGTH = 200


class UserSerializer(serializers.Serializer):
    """Сериализатор для регистрации User."""
    email = serializers.EmailField()
    username = serializers.CharField(
        validators=[validate_username, ]
    )


class ForUserSerializer(serializers.ModelSerializer):
    """Сериализатор для User. Зарезервированное имя использовать нельзя."""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=MAX_LENGTH,
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
    """Сериализатор для Admin. Зарезервированное имя использовать нельзя."""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        max_length=MAX_LENGTH,
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
        max_length=MAX_LENGTH,
        required=True,
        validators=[
            validate_username,
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    confirmation_code = serializers.CharField(
        max_length=MAX_LENGTH, required=True
    )
