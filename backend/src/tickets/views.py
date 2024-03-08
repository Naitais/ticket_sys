#bridge between backend and frontend

from rest_framework.generics import ListAPIView
#from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.generics import DestroyAPIView
from .models import  Registro, Usuario
from .serializer  import TicketSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Registro
from datetime import datetime

#for login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

#muestro tickets
class TicketView(ListAPIView):
    queryset = Registro.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]

def index(request):
    #solo entra al menu de tickets si la variable de sesion es true
    if request.session.get('usuario_logueado'):
        
        regitros = Registro.objects.order_by("id_registro")
        template = loader.get_template("tickets/index.html") #codigo frontend
        context = {"regitros": regitros,
                   "usuario_logueado": request.session['username']} #el contexto son los objetos de python que voy a mostrar
        return render(request, "tickets/index.html", context)
    else:
        return redirect('http://127.0.0.1:8000/api/login/')

def nuevo_ticket(request):
    if request.method == 'POST':
        usuario = request.session['username']
        concepto =request.POST['concepto']
        empresa =request.POST['empresa']
        legajo =request.POST['legajo']
        nombre =request.POST['nombre']
        observaciones =request.POST['observaciones']
    
    nuevo_ticket = Registro(usuario = usuario,concepto= concepto, empresa = empresa, legajo = legajo, nombre = nombre, observaciones = observaciones)
    nuevo_ticket.save()
    return HttpResponse("FUNCIONO")

def modificar_registro(request, id_registro):
    if request.method == 'POST':
        # busco el registro segun la id que paso el usuario
        registro = get_object_or_404(Registro, pk=id_registro)
        
        # sobreescribo los valores del registro con lo nuevo
        registro.concepto = request.POST.get('concepto', registro.concepto)
        registro.empresa = request.POST.get('empresa', registro.empresa)
        registro.legajo = request.POST.get('legajo', registro.legajo)
        registro.nombre = request.POST.get('nombre', registro.nombre)
        registro.observaciones = request.POST.get('observaciones', registro.observaciones)
        registro.estado_liquidaciones = request.POST.get('estado_liquidaciones', registro.estado_liquidaciones)
        registro.fecha_sistemas = datetime.now()
        
        # guardo en la base de datos
        registro.save()
        
        return HttpResponse("Registro actualizado exitosamente.")
    else:
        return HttpResponse("Este endpoint solo acepta solicitudes POST para actualizar registros.")
    
def eliminar_registro(request, id_registro):
    if request.method == 'DELETE':
        registro = get_object_or_404(Registro, pk=id_registro)
        registro.delete()
        return HttpResponse('Registro eliminado con éxito')
    else:
        return HttpResponse('Método no permitido')

def autenticar_login(request):
    if request.method == 'POST':
        usuario_input = request.POST.get('usuario')
        
        contraseña_input = request.POST.get('contraseña')
        
        # filtro todos los usuarios y engancho el primero que coincida con las credenciales del request
        user = Usuario.objects.filter(usuario=usuario_input, contraseña=contraseña_input).first()
        
        #si existen el usuario y la contraseña entonces entra
        if user.usuario and user.contraseña:
            
            #cuando loguea seteo la variable de sesion como true
            # y obtengo el nombre de usuario
            request.session['usuario_logueado'] = True
            request.session['username'] = user.usuario
            #return redirect('http://127.0.0.1:8000/api/tickets/')  # el redirect no me funciona
            return HttpResponse('éxito')
        else:
            
            #error
            return HttpResponse('error')
            
    else:
        
        #eliminamos usuario logueado de la sesion del request solo si existe
        if 'usuario_logueado' in request.session:
            del request.session['usuario_logueado']
            del request.session['username']

        #cuando solo entramos a la pagina y no hay ningun request
        return render(request, 'tickets/login.html')
    
def nuevo_usuario(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña =request.POST['contraseña']
        email =request.POST['email']
    
    nuevo_usuario = Usuario(usuario = usuario,contraseña= contraseña, email = email)
    nuevo_usuario.save()
    return HttpResponse("FUNCIONO")

def historico_tickets(request):
    #solo entra al menu de tickets si la variable de sesion es true
        
    regitros = Registro.objects.order_by("id_registro")
    template = loader.get_template("tickets/historico.html") #codigo frontend
    context = {"regitros": regitros} #el contexto son los objetos de python que voy a mostrar
    return render(request, "tickets/historico.html", context)
