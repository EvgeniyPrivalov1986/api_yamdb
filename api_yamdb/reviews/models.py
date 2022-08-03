from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Review(models.Model):

    SCORE_CHOICES = (
        (1, '1. Очень плохо.'),
        (2, '2. Плохо.'),
        (3, '3. Не очень.'),
        (4, '4. Так себе.'),
        (5, '5. Ни то, ни сё.'),
        (6, '6. Неплохо.'),
        (7, '7. Хорошо.'),
        (8, '8. Очень хорошо.'),
        (9, '9. Великолепно.'),
        (10, '10. Высший балл.'),
    )

    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Введите текст отзыва'
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Отзыв',
        blank=True, null=True,
        help_text='Произведение, к которому относится комментарий',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
        null=True,
    )
    score = models.IntegerField(
        choices=SCORE_CHOICES,
    )

    def __str__(self) -> str:
        return self.text[:20]

class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
        blank=True, null=True,
        help_text='Отзыв, к которому относится комментарий',

    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        null=True,
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.text[:20]

<<<<<<< HEAD
=======
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
    name = models.CharField(
        verbose_name='Произведения, к которым пишут отзывы',
        max_length=300,
    )
    year = models.IntegerField(
        verbose_name='Дата публикации',
        validators=[validate_year,],
    )
    genre = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр',
        related_name='titles',
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name[:15]

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
>>>>>>> 769e7c58af779b7c6afd7cad73bbd7e86a034749
