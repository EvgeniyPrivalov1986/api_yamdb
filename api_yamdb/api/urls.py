<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet
from users.views import APIUser, UserViewSetForAdmin

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('users', UserViewSetForAdmin, basename='users')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('users.urls')),
    path('v1/users/me/', APIUser.as_view(), name='me'),
    path('v1/', include(router_v1.urls)),
]
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet
from users.views import APIUser, UserViewSetForAdmin

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('users', UserViewSetForAdmin, basename='users')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('users.urls')),
    path('v1/users/me/', APIUser.as_view(), name='me'),
    path('v1/', include(router_v1.urls)),
]
>>>>>>> ec6a492bc25a313f0175de82980790c4c319a5cc
