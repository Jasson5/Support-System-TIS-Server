from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

from api import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view()),
    path('api-auth/', views.CustomAuthToken.as_view()),
    url(r'^person/$', views.PersonApi),
    url(r'^person/([0-9]+)$', views.PersonApi),

    url(r'^company/$', views.CompanyApi),
    url(r'^company/([0-9]+)$', views.CompanyApi),

    url(r'^role/$', views.RoleApi),
    url(r'^role/([0-9]+)$', views.RoleApi),

    #path('login', views.login, name="login"),
    #path('registro', views.register, name="registro"),
]

urlpatterns = format_suffix_patterns(urlpatterns)