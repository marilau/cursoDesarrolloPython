from django.db import models

from apps.usuarios.models  import Usuario

class Tag(models.Model):
	nombre = models.CharField(max_length=250)

	class Meta:
		db_table = "tags"

	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=250)

	class Meta:
		db_table = "categorias"

	def __str__(self):
		return self.nombre
"""
class ProductoTag(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
"""

class Producto(models.Model):
	nombre = models.CharField(max_length=250)
	precio = models.DecimalField(max_digits=9, decimal_places=2)
	cantidad = models.IntegerField(default=0)
	
	activo = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to="productos", null=True, blank=True)

	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos_relacionados', null=True)
	tags = models.ManyToManyField(Tag)

	class Meta:
		db_table = "productos"

	def __str__(self):
		return self.nombre

#productos = Producto.objects.all()

class Comentario(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	descripcion = models.CharField(max_length=500)
	
	class Meta:
		db_table = "comentarios"

