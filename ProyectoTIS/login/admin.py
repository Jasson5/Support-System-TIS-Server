from django.contrib import admin
from .models import GrupoEmpresa, Rol, Usuario
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(GrupoEmpresa)

TokenAdmin.raw_id_fields = ['user']