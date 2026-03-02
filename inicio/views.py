from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.


def index(request):
    contexto = {
        "ahora": timezone.localtime(),
        "temas": ["extends/base", "blocks", "variables {{ }}", "tags {% %}", "for/if"],
        "modo": "practica",
    }
    return render(request, "inicio/inicio.html", contexto)
    #return HttpResponse( "Hola 👋 Estás en la app 'inicio'.")


def pato(request):
    return HttpResponse("<h1>🐔Cuak...!!!</h1>")


def acerca(request):
    return render(request, "inicio/acerca.html")
    pass

def temario(request):
    return render(request, "inicio/temario.html")


def tarea2(request):
    contexto = {
        'modulo': 'Desarrollo Web con Django',
        'estudiante': 'Williams Surco',
        'estado': 'En Proceso',
        # Lista de etiquetas para el ciclo for
        'tags': ['Python', 'Django', 'HTML', 'CSS', 'FullStack', 'MVT']
    }
    return render(request, "inicio/tarea2.html", contexto)