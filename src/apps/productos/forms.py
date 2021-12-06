from django import forms

from .models import Producto, Comentario

class ProductoForm(forms.ModelForm):

	nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre del producto"}))
	
	class Meta:
		model = Producto
		fields = ["nombre", "precio", "cantidad", "activo", "imagen"]


class ComentarioForm(forms.ModelForm):

	descripcion = forms.CharField(label="Comentario", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Escriba su comentario"}))
	
	class Meta:
		model = Comentario
		fields = ["descripcion"]