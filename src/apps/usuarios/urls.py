from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
	path("Registrarme/", views.registrar_usuario, name="registrar")
]