from django.http import HttpResponse
from django.template import Template, Context, loader
from AppFamiliares.models import * 
from AppFamiliares.views import *

def Template(request):
    
    lista=["Francisco", "Gonzalez",64,"Maria","Vargas", 62,"Vanesa","Gonzalez",31]
    diccionario= {'lista':lista}
    plantilla= loader.get_template('Template.html')
    documento= plantilla.render(diccionario)

    return HttpResponse(documento)
