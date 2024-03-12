#bridge between backend and frontend

from .models import  Ticket, Usuario
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
import datetime

#funcion para obtener el mes o año de una fecha pasada como string
def obtener_año_o_mes(año_o_mes: str, fecha_string: str):
    if año_o_mes == "año":
        ticket_año: int = fecha_string[0:4]
        return ticket_año
    
    elif año_o_mes == "mes":
        ticket_mes: int = fecha_string[5:7]
        return ticket_mes

def index(request):
    #solo entra al menu de tickets si la variable de sesion es true
    if request.session.get('usuario_logueado'):
        tickets = Ticket.objects.order_by("id_ticket")
        fecha_actual = str(datetime.date.today())

        #obtengo mes actual para pasarlo al front end
        request.session['mes_liquidacion'] = datetime.date.today().month
        request.session['año_liquidacion'] = datetime.date.today().year

        #para guardar los tickets filtrados
        tickets_filtrados: list = []

        #compara cada ticket y solo se queda con los del mes y año actuales
        for ticket in tickets:
            if obtener_año_o_mes("año", ticket.fecha_liquidaciones) == obtener_año_o_mes("año", fecha_actual):
                if obtener_año_o_mes("mes", ticket.fecha_liquidaciones) == obtener_año_o_mes("mes", fecha_actual):
                    tickets_filtrados.append(ticket)

        contexto: dict = {"tickets": tickets_filtrados,
                "usuario_logueado": request.session['username'],
                "mes_liquidacion": request.session['mes_liquidacion'],
                "año_liquidacion": request.session['año_liquidacion']} #el contexto son los objetos de python que voy a mostrar
        return render(request, "tickets/index.html", contexto)
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
    
    nuevo_ticket = Ticket(usuario = usuario,concepto= concepto, empresa = empresa, legajo = legajo, nombre = nombre, observaciones = observaciones)
    nuevo_ticket.save()
    return HttpResponse("FUNCIONO")

def modificar_ticket(request, id_ticket):
    if request.method == 'POST':
        # busco el Ticket segun la id que paso el usuario
        ticket = get_object_or_404(Ticket, pk=id_ticket)
        
        # sobreescribo los valores del Ticket con lo nuevo
        ticket.concepto = request.POST.get('concepto', ticket.concepto)
        ticket.empresa = request.POST.get('empresa', ticket.empresa)
        ticket.legajo = request.POST.get('legajo', ticket.legajo)
        ticket.nombre = request.POST.get('nombre', ticket.nombre)
        ticket.observaciones = request.POST.get('observaciones', ticket.observaciones)
        ticket.estado_liquidaciones = request.POST.get('estado_liquidaciones', ticket.estado_liquidaciones)
        
        # guardo en la base de datos
        ticket.save()
        
        return HttpResponse("Ticket actualizado exitosamente.")
    else:
        return HttpResponse("Este endpoint solo acepta solicitudes POST para actualizar tickets.")
    
def eliminar_ticket(request, id_ticket):
    if request.method == 'DELETE':
        ticket = get_object_or_404(Ticket, pk=id_ticket)
        ticket.delete()
        return HttpResponse('Ticket eliminado con éxito')
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
        #cuando solo entramos a la pagina login y no hay ningun request
        
        #eliminamos usuario logueado de la sesion del request solo si existe
        if 'usuario_logueado' in request.session:
            del request.session['usuario_logueado']
            del request.session['username']

        
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
        
    tickets = Ticket.objects.order_by("id_ticket")
    contexto: dict = {"tickets": tickets} #el contexto son los objetos de python que voy a mostrar
    return render(request, "tickets/historico.html", contexto)

def historico_tickets_consulta(request):
    if request.method == 'POST':
        mes_input = request.POST['mes']
        año_input = request.POST['año']
        
        request.session['consulta_mes_input'] = mes_input
        request.session['consulta_año_input'] = año_input
        #para guardar los tickets filtrados
        
        return HttpResponse("exito")
    else:
        #contexto: dict = {"tickets": tickets} #el contexto son los objetos de python que voy a mostrar
        return render(request, "tickets/historico.html")
    
def consulta_tickets(request):
    tickets = Ticket.objects.order_by("id_ticket")
    if request.session['consulta_mes_input'] and request.session['consulta_año_input']:
        tickets_filtrados: list = []

        #compara cada Ticket y solo se queda con los del mes y año actuales
        for ticket in tickets:
            if obtener_año_o_mes("año", ticket.fecha_liquidaciones) == request.session['consulta_año_input']:
                if obtener_año_o_mes("mes", ticket.fecha_liquidaciones) == request.session['consulta_mes_input']:
                    tickets_filtrados.append(ticket)

        contexto: dict = {"tickets": tickets_filtrados} #el contexto son los objetos de python que voy a mostrar
        return render(request, "tickets/consulta.html", contexto)
    else:
            
        #error
        return render(request, "tickets/consulta.html")