#bridge between backend and frontend

from .models import  Ticket
from .serializer import TicketSerializer

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
import datetime

from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

#para los permisos de rest framework y que no me tire error:
    #Cannot apply DjangoModelPermissionsOrAnonReadOnly on a view that does not set `.queryset` or have a `.get_queryset()` method.

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

#@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
class TicketList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'tickets/index.html'
    
    def get(self, request, format=None):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
    
        return Response({'tickets': serializer.data})
    
    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class TicketList(APIView):
#    """
#    List all tickets.
#    """
#    def get(self, request, format=None):
#        tickets = Ticket.objects.all()
#        serializer = TicketSerializer(tickets, many=True)
#        return Response({'tickets': serializer.data})

    #def post(self, request, format=None):
     #   serializer = TicketSerializer(data=request.data)
      #  if serializer.is_valid():
       #     serializer.save()
       #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class TicketList(APIView):
#    renderer_classes = [TemplateHTMLRenderer]
#    template_name = "tickets/index.html"

#    def get(self, request):
#        queryset = Ticket.objects.all()
#        return Response({'tickets': queryset})

