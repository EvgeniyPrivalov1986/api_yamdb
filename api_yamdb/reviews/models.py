from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категории (типы) произведений',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Уникальная строка идентификатор',
        max_length=50,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name[:15]

