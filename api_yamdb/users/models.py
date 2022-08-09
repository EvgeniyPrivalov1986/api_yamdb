from django.contrib.auth.models import AbstractUser
from django.db import models


USER = "user"
ADMIN = "admin"
MODERATOR = "moderator"

ROLES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)

MAX_LENGTH = 200


class User(AbstractUser):
    """Создает модель пользователя."""
    username = models.CharField(
        unique=True, max_length=MAX_LENGTH, blank=False, verbose_name='username'
    )
    email = models.EmailField('Почта пользователя', unique=True)
    bio = models.TextField('Биография', blank=True)
    role = models.CharField(max_length=20, choices=ROLES, default=USER)
    token = models.CharField(max_length=MAX_LENGTH, blank=True)

    @property
    def is_admin(self):
        return self.is_superuser or self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_user(self):
        return self.role == USER
