from django.urls import path
from .views import index, nuevo_ticket, modificar_registro, eliminar_registro
from explorer.views import query

urlpatterns = [
    path('tickets/', index, name="index"),
    path('nuevo-ticket/', nuevo_ticket, name="nuevo-ticket"),
    path('modificar-ticket/<int:id_registro>/', modificar_registro, name="modificar_registro"),
    path('eliminar-ticket/<int:id_registro>/', eliminar_registro, name="eliminar_registro"),
]

