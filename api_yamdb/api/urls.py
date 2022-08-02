from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import APIUser, UserViewSetForAdmin

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSetForAdmin, basename='users')

urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/users/me/', APIUser.as_view(), name='me'),
    path('v1/', include(router_v1.urls)),
]
