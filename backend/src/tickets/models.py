from django.db import models
import datetime
import getpass

#para tomar el nombre de usuario logueado en la sesion de la persona
username = getpass.getuser()

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField(default=datetime.date.today)
    usuario = models.CharField(max_length=100, default = username)
    concepto = models.IntegerField(default= 0)
    empresa = models.CharField(max_length=100)
    agente_legajo = models.IntegerField(default= 0000000000)
    agente_nombre = models.CharField(max_length=100)
    observaciones = models.TextField(default = ' ')
    estado_ticket = models.CharField(max_length=50, default = 'Pendiente')
    devoluciones = models.TextField(default = ' ')

#ANALIZAR COMO LO VOY A CREAR PORQUE TIENE QUE SER UNA COPIA DE TICKET
#class TicketHistorico(models.Model):
#    id_ticket = models.AutoField(primary_key=True)
#    fecha_creacion = models.DateTimeField("fecha de ticket")
#    fecha_creacion = models.DateTimeField("fecha de ticket")
#    usuario = models.CharField(max_length=100, default = username)
#    concepto = models.IntegerField()
#    empresa = models.CharField(max_length=100)
#    legajo = models.CharField(max_length=50) #deberia ser un entero
#    nombre = models.CharField(max_length=100)
#    observaciones = models.TextField(default = ' ')
#    estado_ticket = models.CharField(max_length=50, default = 'Pendiente')
#    devoluciones = models.TextField(default = ' ')

class UsuarioSistemas(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length = 50)

