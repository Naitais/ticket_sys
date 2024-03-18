from django.urls import path
from . import views

urlpatterns = [
    path('ticketera/', views.TicketList.as_view(), name='ticket-list'),
    
]


