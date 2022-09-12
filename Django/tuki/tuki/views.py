from datetime import datetime
from pipes import Template
from re import template
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render

class Persona(object):
    def __init__(self, Nombre, Apellido):
        self.nombre=Nombre
        self.apellido=Apellido

def hola(request):
    p1=Persona("Xavi Juan", "Messi")
    #Nombre="Juan"
    #Apellido="Messi"
    temasaver=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    Now=datetime.datetime.now()
    #doc_externo=open("C:/Users/PoloBaradero1/Desktop/Django/tuki/tuki/Plantillas/plantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=get_template("plantilla.html")
    #ctx=Context({"nombre_man":p1.nombre, "apellido":p1.apellido, "actual":Now, "temas":temasaver})
    #Documento=doc_externo.render({"nombre_man":p1.nombre, "apellido":p1.apellido, "actual":Now, "temas":temasaver})
    return render(request, "plantilla.html", {"nombre_man":p1.nombre, "apellido":p1.apellido, "actual":Now, "temas":temasaver})

def cursoA(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoA.html", {"damefecha":fecha_actual})

def cursoB(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoB.html", {"damefecha":fecha_actual})

def adios(request):
    return HttpResponse("nos vemos")

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    Documento="""<html>
    <body>
    <h2>
    Fecha y Hora Actuales %s
    </h2>
    </body>
    </html>"""% fecha_actual
    return HttpResponse(Documento)

def CalcularEdad(request,edad,agno):
    #EdadActual=18
    Período=agno-2022
    EdadFutura=edad+Período
    Documento="""<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>"""%(agno, EdadFutura)
    return HttpResponse(Documento)