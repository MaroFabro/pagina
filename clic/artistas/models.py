from django import forms
from typing_extensions import Required
from django.db import models

# Create your models here.

class Inscripcion(models.Model):
    Nombre_de_banda_o_artista=models.CharField (max_length=30), (Required)
    Cantidad_de_integrantes=models.IntegerField()
    Infromación_artística_o_reseña=models.CharField(max_length=255), (Required)
    Rubro_o_género_de_música=models.CharField(max_length=100), (Required)
    Provincia=models.CharField(max_length=50)
    Localidad=models.CharField(max_length=50)
    Contacto_telefónico=models.CharField(max_length=15), (Required)
    Contacto_Mail=models.EmailField(Required)
    Link_o_sitios_de_material_discográfico=models.CharField(max_length=1000)
    Razón_social=models.CharField(max_length=255)
    Costos=models.IntegerField(Required)