from django.contrib import admin

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
	list_display = ["nombre", "precio", "cantidad", "activo"]

admin.site.register(Producto, ProductoAdmin)