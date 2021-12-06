from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render, redirect
from django.urls                    import reverse_lazy
from django.views.generic           import ListView, CreateView
from django.views.generic.edit      import UpdateView
from django.views.generic.detail    import DetailView

from apps.core.decorators import superuser_required
from apps.core.mixins import SuperUserRequiredMixin

from .forms import ProductoForm, ComentarioForm
from .models import Producto, Categoria, Comentario

"""
@login_required
def listar(request):
	template_name = "productos/listar.html"
	contexto = {
		"nombre_usuario": "Marilau",
		"lista_productos": Producto.objects.all()
	}
	return render(request, template_name, contexto)
"""

class Listar(LoginRequiredMixin, ListView):
	template_name = "productos/listar.html"
	model = Producto
	context_object_name = 'lista_productos'
	paginate_by = 5

	def get_queryset(self):
		return Producto.objects.filter(activo=True).order_by("nombre")

# ========================================================
#                  Vistas para Admin
# ========================================================


class ListarAdmin(SuperUserRequiredMixin, LoginRequiredMixin, ListView):
	template_name = "productos/admin/listar.html"
	model = Producto
	context_object_name = 'lista_productos'
	paginate_by = 5

	def get_queryset(self):
		return Producto.objects.all().order_by("id")


class Crear(SuperUserRequiredMixin, LoginRequiredMixin, CreateView):
	template_name = "productos/admin/nuevo.html"
	model = Producto
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")

class Editar(LoginRequiredMixin, UpdateView):
	template_name = "productos/admin/editar.html"
	model = Producto
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")

class Detalle(SuperUserRequiredMixin, LoginRequiredMixin, DetailView):
	model = Producto
	template_name = "productos/admin/detalle.html"

@superuser_required()
def borrar(request, pk):
	p = Producto.objects.get(id=pk)
	p.delete()
	return redirect("productos:admin_listar")

# ========================================================
#                  Vistas para Comentario
# ========================================================

class VerProducto(DetailView):
	model = Producto
	template_name = "productos/ver.html"

class ListarComentarios(ListView):
	template_name = "productos/comentarios/listar.html"
	model = Comentario
	context_object_name = 'lista_comentarios'
	paginate_by = 5

	def get_queryset(self):
		return Comentario.objects.all().order_by("id")

class CrearComentario(LoginRequiredMixin, CreateView):
	template_name = "productos/comentarios/nuevo.html"
	model = Comentario
	form_class = ComentarioForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")

class EditarComentario(LoginRequiredMixin, UpdateView):
	template_name = "productos/comentarios/editar.html"
	model = Comentario
	form_class = ComentarioForm

def borrar_comentario(request, pk):
	c = Comentario.objects.get(id=pk)
	c.delete()
	return redirect("productos:listar")