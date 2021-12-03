from django.shortcuts          import render
from django.views.generic.list import ListView

from .models import Producto

"""
def listar(request):
	template_name = "productos/listar.html"
	contexto = {
		"nombre_usuario": "Marilau",
		"lista_productos": Producto.objects.all()
	}
	return render(request, template_name, contexto)
"""

class Listar(ListView):
	template_name = "productos/listar.html"
	model = Producto
	context_object_name = 'lista_productos'
	paginate_by = 2