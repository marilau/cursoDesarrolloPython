from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.usuarios.models import Usuario

class UsuarioForm(UserCreationForm):
	username = forms.CharField(label="Usuario", required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese nombre de usuario"}))
	first_name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su nombre"}))
	last_name = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su apellido"}))
	email = forms.EmailField(label="Correo", required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su correo electrónico"}))
	password1 = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Ingrese su contraseña"}))
	password2 = forms.CharField(label="Repita su contraseña", required=True, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Repita su contraseña"}))
	
	class Meta:
		model = Usuario
		fields = ("first_name", "last_name", "username", "email")