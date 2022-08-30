from django.http import HttpResponse
from django.shortcuts import render
from AppFamiliares.models import *
# Create your views here.class Familiar(models.Model):
    #nombre= models.CharField(max_length=50)
    #apellido= models.CharField(max_length=50)
    #edad= models.IntegerField()
    #año_de_nacimiento= models.IntegerField(datetime ) 
def Familiares(self):

    Familiar_1= Familiar(nombre="Francisco", apellido="Gonzalez", edad=64)
    Familiar_1.save()
    texto=f"Familiar {nombre} {apellido} de {edad} años"
    return HttpResponse(texto)

def Familiares(self):
    Familiar_2= Familiar(nombre="Maria", apellido="Vargas", edad=62)
    Familiar_2.save()
    texto=f"Familiar {nombre} {apellido} de {edad} años"
    return HttpResponse(texto)

def Familiares(self):
    Familiar_3= Familiar(nombre="Vanesa", apellido="Gonzalez", edad=31)
    Familiar_3.save()
    texto=f"Familiar {nombre} {apellido} de {edad} años"
    return HttpResponse(texto)

