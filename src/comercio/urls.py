from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Productos/', include('apps.productos.urls')),
    path('', views.inicio, name="inicio"),
]
