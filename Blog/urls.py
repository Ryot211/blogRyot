from django.urls import path
from . import views  # Asegúrate de que estás importando las vistas correctas

urlpatterns = [
   path("registro/", views.registro, name="registro"),
   path('logout/', views.mi_logout, name='logout'),
   path('',views.listadoArticulo),
   path('CrearArticulo/',views.CrearArticulo),
    
   
]