from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> ec6a492bc25a313f0175de82980790c4c319a5cc
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/', include('api.urls'))
]
