from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
	#path("ListarProductos/", views.listar, name="listar")
	path("ListarProductos/", views.Listar.as_view(), name="listar"),
]