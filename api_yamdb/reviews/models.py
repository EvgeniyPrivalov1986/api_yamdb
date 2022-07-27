from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    ROLES_CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)    
    email = models.EmailField(
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    roles = models.CharField(
        max_length=255,
        choices=ROLES_CHOICES,
        default='user',
        verbose_name='Роль'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_user(self):
        return self.role == 'user'