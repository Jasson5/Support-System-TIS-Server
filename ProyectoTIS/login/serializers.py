from rest_framework import serializers
from login.models import Usuario, GrupoEmpresa, Rol

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (  'usuarioId',
                    'nombre',
                    'apellidos',
                    'correo',
                    'contrasenia',
                    'rol_usr',
                    'grupo_usr')

class  GrupoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoEmpresa
        fields = (  'grupoId',
                    'nombre',
                    'telefono',
                    'direccion',
                    'correoEmpresa')

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = (  'rolId',
                    'tipoRol')


