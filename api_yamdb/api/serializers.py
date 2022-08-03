from rest_framework import serializers
from reviews.models import Review, Comment
from reviews.models import Category, Genre, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        title = int(data['title'])
        author = self.context['request'].user
        if Review.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв к этому произведению.'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'review', 'pub_date')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True     
    )

    class Meta:
        model = Title,
        fields = '__all__'


class ReadTitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True,
    )
    genre = GenreSerializer(
        read_only=True,
    )
    # rating = serializers.IntegerField(
    #     source='reviews__score__avg',
    #     read_only=True,
    # )

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
