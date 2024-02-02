#bridge between backend and frontend

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Ticket
from .serializer  import TicketSerializer

class TicketView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class NuevoTicket(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]