from django.shortcuts import render
from .models import Articulo

#Articulo
def listadoArticulo (request):
    articulosBdd= Articulo.objects.all()
    return render (request, "ListarBlog.html",{'articuloss':articulosBdd})

# Create your views here.
