#bridge between backend and frontend

from .models import  Ticket
from .serializer import TicketSerializer
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

#para los permisos de rest framework y que no me tire error:
    #Cannot apply DjangoModelPermissionsOrAnonReadOnly on a view that does not set `.queryset` or have a `.get_queryset()` method.

from rest_framework.decorators import api_view, permission_classes


from rest_framework import generics

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ticketera': reverse('ticket-lista', request=request, format=format)
    })

from rest_framework import renderers

class TicketHighlight(generics.GenericAPIView):
    queryset = Ticket.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        ticket = self.get_object()
        return Response(ticket.highlighted)