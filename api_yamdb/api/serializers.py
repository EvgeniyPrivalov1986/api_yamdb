from rest_framework import serializers

from reviews.models import Category, Genre, Title


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
        model = Title,
        fields = '__all__'