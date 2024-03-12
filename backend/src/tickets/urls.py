from django.urls import path
from .views import index, nuevo_ticket, modificar_ticket, eliminar_ticket, autenticar_login, nuevo_usuario, historico_tickets,historico_tickets_consulta, consulta_tickets

urlpatterns = [
    path('tickets/', index, name="index"),
    path('nuevo-ticket/', nuevo_ticket, name="nuevo_ticket"),
    path('modificar-ticket/<int:id_ticket>/', modificar_ticket, name="modificar_ticket"),
    path('eliminar-ticket/<int:id_ticket>/', eliminar_ticket, name="eliminar_ticket"),
    path('login/', autenticar_login, name="login"),
    path('nuevo-usuario/', nuevo_usuario, name="nuevo_usuario"),
    path('historico-tickets/', historico_tickets_consulta, name="historico_tickets"),
    path('consulta-tickets/', consulta_tickets, name="consulta_tickets"),
    
]

