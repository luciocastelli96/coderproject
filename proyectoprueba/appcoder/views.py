from django.shortcuts import render
from .models import curso
from django.http import HttpResponse

# Create your views here.

def curso(request):
    mi_curso= curso(nombre="css", camada= 22551)
    mi_curso.save()
    return HttpResponse(f'se genero el curso de {mi_curso.nombre} con la camada {mi_curso.camada}')
