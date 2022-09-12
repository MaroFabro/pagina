from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from artistas.forms import FormularioContacto, Inscripción
from typing_extensions import Required

# Create your views here.


def formularios(request):
    elformulario=Inscripción()
    if request.method=="POST": 
        elformulario=Inscripción(request.POST)
        if elformulario.is_valid():
            print("Valido")
        return render(request, "gracias.html")
    else:
        elformulario=Inscripción()
    return render(request, "formularios.html", {"form":elformulario})


def contacto(request):
    if request.method=="POST":
        miformulario=FormularioContacto(request.POST)
        if miformulario.is_valid():
            infForm=miformulario.cleaned_data
            send_mail(infForm["asunto"], infForm["mensaje"],
            infForm.get("email",''),["fabrimaroli@gmail.com"])
        return render(request, "gracias.html")

    else:
            miformulario=FormularioContacto()
    return render(request, "contacto.html",{"form":miformulario})
    
    
