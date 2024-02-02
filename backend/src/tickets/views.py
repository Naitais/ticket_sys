#bridge between backend and frontend

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Ticket
from .serializer  import TicketSerializer

class TicketView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer