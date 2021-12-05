from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=250)

	class Meta:
		db_table = "categorias"

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=250)
	precio = models.DecimalField(max_digits=9, decimal_places=2)
	cantidad = models.IntegerField(default=0)
	
	activo = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to="productos", null=True, blank=True)

	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos_relacionados', null=True)

	class Meta:
		db_table = "productos"

	def __str__(self):
		return self.nombre

#productos = Producto.objects.all()

