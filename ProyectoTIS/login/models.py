from django.db import models
from django.db.models.base import Model

# Create your models here.

    
class GrupoEmpresa(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=50)
    correoELectronicoEmpresa =models.EmailField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
       verbose_name='grupoEmpresa'
       verbose_name_plural='gruposEmpresas'


class Rol(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    tipoDeRol=models.CharField(max_length=50)
    def __str__(self):
       return self.tipoDeRol
    class Meta:
       verbose_name='rol'
       verbose_name_plural='roles'


class Usuario(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    correo =models.EmailField(max_length=50)
    contrasenia=models.CharField(max_length=50)
    Rol_usr=models.ForeignKey(Rol,null=False, blank=False , on_delete=models.CASCADE) 
    grupo_usr=models.ForeignKey(GrupoEmpresa,null=False, blank=False, on_delete=models.CASCADE) #no tiene grupo=0
    def __str__(self):
       return self.nombre
    class Meta:
       verbose_name='usuario'
       verbose_name_plural='usuarios'