from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class MyUserManager(UserManager):
    """Сохраняет пользователя только с email."""
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле email обязательное')
        return super().create_user(
            username, email=email, password=password, **extra_fields
        )

    def create_superuser(
        self, username, email, password, role='admin', **extra_fields
    ):
        return super().create_superuser(
            username, email, password, role='admin', **extra_fields
        )


class User(AbstractUser):
    """Создает модель пользователя."""
    ROLES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    REQUIRED_FIELDS = ('email', 'password')
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=200, choices=ROLES, default='user')
    username = models.CharField(max_length=150, unique=True, db_index=True)
    objects = MyUserManager()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.role == self.ROLES[2][0]

    @property
    def is_moderator(self):
        return self.role == self.ROLES[1][0]
