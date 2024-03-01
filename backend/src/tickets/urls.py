from django.urls import path
from .views import index, nuevo_ticket, mostrar_registro_por_id

urlpatterns = [
    path('tickets/', index, name="index"),
    path('nuevo-ticket/', nuevo_ticket, name="nuevo-ticket"),
    path('registro/', mostrar_registro_por_id, name="mostrar_registro_por_id"),
]