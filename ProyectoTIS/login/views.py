from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def login(request):
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
    return render(request, "registro.html", context)
# Create your views here.
