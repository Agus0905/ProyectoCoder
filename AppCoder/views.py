from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Curso(self):
    curso = Curso(nombre = "Desarollo web", camada = "1960")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)