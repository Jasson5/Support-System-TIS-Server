from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("login")

#primer spr
def home(request):
    return render(request, "home.html")

def crearPublicacion(request):
    return render(request, "crearPublicaciones.html")

def empresasHistoricas(request):
     return render(request, "empresasHistoricas.html")
#fin primer sprint
