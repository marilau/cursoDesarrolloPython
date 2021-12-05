from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	foto = models.ImageField(upload_to="perfil", null=True)

	class Meta:
		db_table = "usuarios"

	def __str__(self):
		return self.get_full_name()