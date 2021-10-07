from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from login import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view()),
    path('api-auth/', views.CustomAuthToken.as_view()),
    path('login', views.login, name="login"),
    path('registro', views.register, name="registro"),
]

urlpatterns = format_suffix_patterns(urlpatterns)