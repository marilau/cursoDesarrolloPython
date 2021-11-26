from django.db import models

# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=250)
	precio = models.DecimalField(max_digits=9, decimal_places=2)
	cantidad = models.IntegerField(default=0)

	class Meta:
		db_table = "productos"

	def __str__(self):
		return self.nombre

#productos = Producto.objects.all()
