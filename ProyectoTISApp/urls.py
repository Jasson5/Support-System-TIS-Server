from django.urls import path
from ProyectoTISApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('crearPublicacion', views.crearPublicacion, name="crearPublicacion"),
    path('empresasHistoricas', views.empresasHistoricas, name="empresasHistoricas"),
]
