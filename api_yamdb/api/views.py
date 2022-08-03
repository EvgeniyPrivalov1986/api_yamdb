from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
#from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Avg
from reviews.models import Review, Title, User
from reviews.models import Category, Genre, Title
from api.serializers import CommentSerializer, ReviewSerializer
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer, ReadTitleSerializer
from api.permissions import AuthorOrAdminOrReadOnly
from .permissions import IsAdminOrReadOnly
from .firters import TitlesFilter

from django_filters.rest_framework import DjangoFilterBackend


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AuthorOrAdminOrReadOnly,)

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        serializer.save(author=self.request.user, title=title)



class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrAdminOrReadOnly,)

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        serializer.save(author=self.request.user, review=review)




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    # queryset = Title.objects.annotate(
    #     Avg('reviews__score')
    # )
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadTitleSerializer
        return TitleSerializer
>>>>>>> 769e7c58af779b7c6afd7cad73bbd7e86a034749
