from django import forms
from typing_extensions import Required
class Inscripción(forms.Form):

    Nombre_de_banda_o_artista=forms.CharField(max_length=30)
    Cantidad_de_integrantes=forms.IntegerField()
    Infromación_artística_o_reseña=forms.CharField(max_length=255)
    Rubro_o_género_de_música=forms.CharField(max_length=100)
    Provincia=forms.CharField(max_length=40)
    Localidad=forms.CharField(max_length=40)
    Contacto_telefónico=forms.CharField(max_length=15)
    Contacto_Mail=forms.EmailField()
    Link_o_sitios_de_material_discográfico=forms.CharField(max_length=1000)
    Razón_social=forms.CharField(max_length=255)
    Costos=forms.IntegerField()

class FormularioContacto(forms.Form):

    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()