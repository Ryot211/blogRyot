from django.db import models
from django.contrib.auth.models import User

#Articulo
class Articulo(models.Model):
    id_art =models.AutoField(primary_key=True)
    titulo_art = models.CharField(max_length=100)
    contenido_art=models.CharField(max_length=350)
    autor_art=models.ForeignKey(User, on_delete=models.CASCADE)
    creacion_art=models.DateField(auto_now_add=True)
    actualizacion_art=models.DateField(auto_now=True)
#Comentario
class Comentario(models.Model):
    id_comen= models.AutoField(primary_key=True)
    articulo=models.ForeignKey(Articulo, null=True,blank=True,on_delete=models.PROTECT)
    autor_comen=models.ForeignKey(User,on_delete=models.CASCADE)
    contenido_comen= models.CharField(max_length=250)
    creacion_comen=models.DateField(auto_now_add=True)
