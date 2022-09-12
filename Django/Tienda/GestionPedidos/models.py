from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    dirección=models.CharField(max_length=50)
    email=models.EmailField()
    tgno=models.CharField(max_length=7)

class Artículos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    número=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()