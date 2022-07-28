from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
