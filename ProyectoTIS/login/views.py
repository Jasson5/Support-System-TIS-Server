from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from login.models import Usuario, GrupoEmpresa, Rol
from login.serializers import UsuarioSerializer, GrupoEmpresaSerializer, RolSerializer

'''def login(request):
    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data ['username']
            messages.success(request, f'Usario {username} creado')
    else:
        form = UserCreationForm()
    context={'form' : form}
    return render(request, "registro.html", context)'''
# Create your views here.

@csrf_exempt
def UsuarioApi(request, id=0):
    if request.method=='GET':
        usuario = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuario, many=True)
        return  JsonResponse(usuario_serializer.data, safe=False)

    elif request.method=='POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        usuario_data = JSONParser().parse(request)
        usuario = Usuario.objects.get(usuarioId=usuario_data['usuarioId'] )
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        usuario = Usuario.objects.get(usuarioId=id)
        usuario.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)


@csrf_exempt
def GrupoEmpresaApi(request, id=0):
    if request.method=='GET':
        grupoempresa = GrupoEmpresa.objects.all()
        grupoempresa_serializer = GrupoEmpresaSerializer(grupoempresa, many=True)
        return  JsonResponse(grupoempresa_serializer.data, safe=False)

    elif request.method=='POST':
        grupoempresa_data = JSONParser().parse(request)
        grupoempresa_serializer = GrupoEmpresaSerializer(data=grupoempresa_data)
        if grupoempresa_serializer.is_valid():
            grupoempresa_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        grupoempresa_data = JSONParser().parse(request)
        grupoempresa = GrupoEmpresa.objects.get(grupoId=grupoempresa_data['grupoId'] )
        grupoempresa_serializer = GrupoEmpresaSerializer(grupoempresa, data=grupoempresa_data)
        if grupoempresa_serializer.is_valid():
            grupoempresa_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        grupoempresa = GrupoEmpresa.objects.get(grupoId=id)
        grupoempresa.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)


@csrf_exempt
def RolApi(request, id=0):
    if request.method=='GET':
        rol = Rol.objects.all()
        rol_serializer = RolSerializer(rol, many=True)
        return  JsonResponse(rol_serializer.data, safe=False)
        
    elif request.method=='POST':
        rol_data = JSONParser().parse(request)
        rol_serializer = RolSerializer(data=rol_data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        rol_data = JSONParser().parse(request)
        rol = Rol.objects.get(rolId=rol_data['rolId'] )
        rol_serializer = RolSerializer(rol, data=rol_data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method=='DELETE':
        rol = Rol.objects.get(rolId=id)
        rol.delete()
        return JsonResponse("Deleted Succesfully!", safe=False)


class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user.email),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_id': user.pk,
            'email': user.email
        })