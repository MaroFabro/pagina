from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Artículos

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje="Artículo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto)>20:
            mensaje="Texto de búsqueda demasiado largo"
        else:
        artículos=Artículos.objects.filter(nombre__icontains=producto)
        return render(request, "resultados_busqueda.html", {"artículos":artículos, "query":producto})
    else:
        mensaje="No has introducido nada"
    return HttpResponse(mensaje)