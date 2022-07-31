from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import APIUser, UserViewSetForAdmin

router = DefaultRouter()
router.register('users', UserViewSetForAdmin, basename='users')

urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/users/me/', APIUser.as_view(), name='me'),
    path('v1/', include(router.urls)),
]
