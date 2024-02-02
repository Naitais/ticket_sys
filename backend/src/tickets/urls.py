from django.urls import path
from .views import TicketView, NuevoTicket
#from .services import services

urlpatterns = [
    path('tickets/', TicketView.as_view(), name='mostrar-ticket'),
    path('create-ticket/', NuevoTicket.as_view(), name='create-ticket'),
    #path('create-note/', services.create_note, name='create-new-note'),
    # Add other URL patterns as needed
]