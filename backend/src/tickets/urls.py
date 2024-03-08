from django.urls import path
from .views import index, nuevo_ticket, modificar_registro, eliminar_registro, autenticar_login, nuevo_usuario, historico_tickets

urlpatterns = [
    path('tickets/', index, name="index"),
    path('nuevo-ticket/', nuevo_ticket, name="nuevo_ticket"),
    path('modificar-ticket/<int:id_registro>/', modificar_registro, name="modificar_registro"),
    path('eliminar-ticket/<int:id_registro>/', eliminar_registro, name="eliminar_registro"),
    path('login/', autenticar_login, name="login"),
    path('nuevo-usuario/', nuevo_usuario, name="nuevo_usuario"),
    path('historico-tickets/', historico_tickets, name="historico_tickets"),
]

