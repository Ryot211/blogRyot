from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.db.models import ProtectedError
from django.contrib import messages
from .models import Articulo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout


def mi_logout(request):
    logout(request)
    return render(request, "registration/logged_out.html")

#registro de usuarios
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # iniciar sesión tras registrarse
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, "registration/registro.html", {"form": form})

#Articulo



def listadoArticulo (request):
    articulosBdd= Articulo.objects.all().order_by('-creacion_art')
    return render (request, "Inicio.html",{'articulos':articulosBdd})

@login_required
def listadoArticuloUser(request):
    if request.user.is_authenticated:
        articulosBdd = Articulo.objects.filter(autor_art=request.user).order_by('-creacion_art')
        return render (request,"Muro.html",{"articulos":articulosBdd})
    else:
        return render(request, "Muro.html", {"articulos": []})
    


@login_required
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
        return redirect("/UserArt/")
    # Si no es POST, mostrar el formulario vacío
    return render(request, "Muro.html")
# Create your views here.


def EliminarArticulo(request,id_art):
    articuloEliminar=Articulo.objects.get(id_art=id_art)
    try:
        articuloEliminar.delete()
        messages.success(request,'Articulo Eliminado')
    except ProtectedError:
        messages.error(request, "No se puede eliminar.")
   
    return redirect("/UserArt/")

def editarArticulo(request,id_art):
    articuloEditar= Articulo.objects.get(id_art=id_art)
    return render(request,'Muro.html',{'articulos':articuloEditar})

def procesarActualizacionArticulo(request):
    id_art=request.POST["id_art"]
    titulo_art = request.POST["titulo_art"]
    contenido_art = request.POST["contenido_art"]
    articuloEditar=Articulo.objects.get(id_art=id_art)
    articuloEditar.titulo_art=titulo_art
    articuloEditar.contenido_art=contenido_art
    articuloEditar.save()
    messages.success(request,'Post Actualizado')
    return redirect('/')


