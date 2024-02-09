#bridge between backend and frontend

from rest_framework.generics import ListAPIView
#from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.generics import DestroyAPIView
from .models import  Registro
from .serializer  import TicketSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Registro

#muestro tickets
class TicketView(ListAPIView):
    queryset = Registro.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]

def index(request):
    regitros = Registro.objects.order_by("id_registro")
    template = loader.get_template("tickets/index.html") #codigo frontend
    context = {"regitros": regitros} #el contexto son los objetos de python que voy a mostrar
    return render(request, "tickets/index.html", context)

def nuevo_ticket(request):
    if request.method == 'POST':
        concepto =request.POST['concepto']
        empresa =request.POST['empresa']
        legajo =request.POST['legajo']
        nombre =request.POST['nombre']
        observaciones =request.POST['observaciones']
    
    nuevo_ticket = Registro(concepto= concepto, empresa = empresa, legajo = legajo, nombre = nombre, observaciones = observaciones)
    nuevo_ticket.save()
    return HttpResponse("FUNCIONO")