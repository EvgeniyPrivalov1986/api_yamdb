from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категории (типы) произведений',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Уникальная строка идентификатор категории',
        max_length=50,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name[:15]


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Категории жанров',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Уникальная строка идентификатор жанра',
        max_length=50,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name[:15]
