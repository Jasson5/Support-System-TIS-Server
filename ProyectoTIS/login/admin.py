from django.contrib import admin
from .models import GrupoEmpresa, Rol, Usuario
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(GrupoEmpresa)
