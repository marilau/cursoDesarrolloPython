from django.urls import path

from . import views

app_name = "productos"

urladmin = [
	path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
	path("Admin/Nuevo/", views.Crear.as_view(), name="admin_nuevo"),
	path("Admin/Editar/<int:pk>/", views.Editar.as_view(), name="admin_editar"),
	path("Admin/Borrar/<int:pk>/", views.borrar, name="admin_borrar"),
	path("Admin/Detalle/<int:pk>/", views.Detalle.as_view(), name="admin_detalle"),
]

urlsitio = [
	#path("ListarProductos/", views.listar, name="listar")
	path("ListarProductos/", views.Listar.as_view(), name="listar"),
]

urlpatterns = urladmin + urlsitio