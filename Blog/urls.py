from django.urls import path
from . import views  # Asegúrate de que estás importando las vistas correctas

urlpatterns = [
   path("registro/", views.registro, name="registro"),
   path('logout/', views.mi_logout, name='logout'),
   path('',views.listadoArticulo),
   path('UserArt/',views.listadoArticuloUser),
   path("CrearArticulo/", views.CrearArticulo, name="crear_articulo"),  # 👈 el name es clave
   path('EliminarArticulo/<id_art>/',views.EliminarArticulo)
    
   
]