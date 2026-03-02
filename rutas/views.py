from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

# Create your views here.

def indice(request):
    return HttpResponse("✅ Laboratorio de rutas activo. Ve a /rutas/ayuda/")

def ayuda(request):
    return HttpResponse(
        "Rutas disponibles: /rutas/hola/, /rutas/hola//, "
        "/rutas/suma///, /rutas/buscar/?q=..., /rutas/api/estado/"
    )



def hora_actual(request):
    # timezone.localtime() usa el TIME_ZONE definido en settings.py ('America/La_Paz')
    ahora = timezone.localtime()
    return HttpResponse(f"🕒 Hora local: {ahora:%Y-%m-%d %H:%M:%S}")


def hola_mundo(request):
    return HttpResponse("<h1>Hola mundo...!!!!</h1> <br>"+
    "<h1>Williams Rodrigo Surco Nina</h1>")


def hola(request):
    return HttpResponse("Hola nadie")

def hola_nombre(request, nombre):
    return HttpResponse(f"hola {nombre}...!!!!")

def suma(request, a, b):
    return HttpResponse(f"la suma es: {a + b}")


def buscar(request):
    q = request.GET.get("q","").strip()

    if not q:
        return HttpResponse("Error envia un query: /rutas/buscar/?q=django")
    
    return HttpResponse(f"Buscando: {q}")


def metodo(request):

    if request.method == 'GET':
        return HttpResponse("uSA get")
    
    if request.method == 'POST':
        return ("estas enviando POST")
    
    return HttpResponse(f"matrodo suado {request.method}")


def api_estado(request):
    data = {
        "estado":"ok",
        "app":"rutas",
        "ruta":request.path,
        "metodo": request.method,
    }
    return JsonResponse(data)

def edad(request, edad):
    if edad < 0 or edad > 120:
        return HttpResponse("Edad invalida", status = 400)
    
    return HttpResponse(f"edad valida: {edad}")

def tabla(request, n ):
    chain = ""
    for i in range(1,11):
        chain += f"{n} x {i} = {n*i}</br>"

    return HttpResponse(chain)
