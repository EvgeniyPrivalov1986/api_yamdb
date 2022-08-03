from django.db import models

from .validators import validate_year


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


class Title(models.Model):
    # name = models.CharField(
    #     verbose_name='Произведения, к которым пишут отзывы',
    #     max_length=300,
    # )
    # year = models.IntegerField(
    #     verbose_name='Дата публикации',
    #     validators=[validate_year],
    # )
    # genre = models.ManyToManyField(
    #     Genre,
    #     verbose_name='Жанр',
    #     related_name='titles',
    # )
    # category = models.ForeignKey(
    #     Category,
    #     verbose_name='Категория',
    #     on_delete=models.SET_NULL,
    #     related_name='titles',
    #     blank=True,
    #     null=True,
    # )
    # description = models.TextField(
    #     verbose_name='Описание',
    #     blank=True,
    #     null=True,
    # )
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    year = models.IntegerField(
        verbose_name='Дата выхода',
        validators=[validate_year]
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles'
        # through='GenreTitle'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None
    )

    def __str__(self):
        return self.name[:15]

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


# class GenreTitle(models.Model):
#     title = models.ForeignKey(
#         Title,
#         verbose_name='Произведение',
#         on_delete=models.CASCADE)
#     genre = models.ForeignKey(
#         Genre,
#         verbose_name='Жанр',
#         on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.title}, жанр - {self.genre}'