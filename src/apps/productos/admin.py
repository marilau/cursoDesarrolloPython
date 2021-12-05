from django.contrib import admin

from .models import Producto, Categoria, Tag

class ProductoAdmin(admin.ModelAdmin):
	list_display = ["nombre", "precio", "cantidad", "activo"]

admin.site.register(Producto, ProductoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ["nombre"]

admin.site.register(Categoria, CategoriaAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ["id","nombre"]

admin.site.register(Tag, TagAdmin)