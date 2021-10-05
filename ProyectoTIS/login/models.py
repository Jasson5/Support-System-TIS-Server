from django.db import models
from django.db.models.base import Model

# Create your models here.
class Usuario(models.Model):
   nombre=models.CharField(max_length=50)
   apellidos=models.CharField(max_length=50)
   correo =models.EmailField(max_length=50)
   contrasenia=models.CharField(max_length=50)
   def __str__(self):
       return self.nombre
   class Meta:
       verbose_name='usuario'
       verbose_name_plural='usuarios'
    
