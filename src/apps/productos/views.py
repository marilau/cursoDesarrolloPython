from django.shortcuts import render

from .models import Producto

# Create your views here.

def listar(request):
	template_name = "productos/listar.html"
	contexto = {
		"nombre_usuario": "Marilau",
		"lista_productos": Producto.objects.all()
	}
	return render(request, template_name, contexto)