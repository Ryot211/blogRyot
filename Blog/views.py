from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Articulo

#Articulo
def listadoArticulo (request):
    articulosBdd= Articulo.objects.all()
    
    return render (request, "Muro.html",{'articuloss':articulosBdd})

def CrearArticulo(request):
    if request.method == "POST":
        titulo_art = request.POST["titulo_art"]
        contenido_art = request.POST["contenido_art"]
        articulo = Articulo(
            titulo_art=titulo_art,
            contenido_art=contenido_art,
            autor_art=request.user
        )
        articulo.save()
        messages.success(request,"Post Creado")
        return redirect("/")  
# Create your views here.
