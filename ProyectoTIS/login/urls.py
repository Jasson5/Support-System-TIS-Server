from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

from login import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view()),
    path('api-auth/', views.CustomAuthToken.as_view()),
    url(r'^usuario/$', views.UsuarioApi),
    url(r'^usuario/([0-9]+)$', views.UsuarioApi),

    url(r'^grupoempresa/$', views.GrupoEmpresaApi),
    url(r'^grupoempresa/([0-9]+)$', views.GrupoEmpresaApi),

    url(r'^rol/$', views.RolApi),
    url(r'^rol/([0-9]+)$', views.RolApi),

    #path('login', views.login, name="login"),
    #path('registro', views.register, name="registro"),
]

urlpatterns = format_suffix_patterns(urlpatterns)