from django.urls import path
from . import views  # Asegúrate de que estás importando las vistas correctas

urlpatterns = [
   path('',views.listadoArticulo)
]