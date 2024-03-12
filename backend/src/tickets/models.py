from django.db import models
import datetime
import getpass

#para tomar el nombre de usuario logueado en la sesion de la persona
username = getpass.getuser()

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    fecha_liquidaciones = models.TextField(default = datetime.date.today) #deberia ser fecha
    usuario = models.CharField(max_length=100)
    concepto = models.CharField(max_length=100) #deberia ser un entero
    empresa = models.CharField(max_length=100)
    legajo = models.CharField(max_length=50) #deberia ser un entero
    nombre = models.CharField(max_length=100)
    observaciones = models.TextField(default = ' ')
    estado_liquidaciones = models.CharField(max_length=50, default = 'Pendiente')
    #operador_sistemas = models.CharField(max_length=100, default = ' ')
    #estado_sistemas = models.CharField(max_length=50, default = ' ')
    #devoluciones = models.TextField(default = ' ')
    #fecha_sistemas = models.TextField(default = ' ')

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length = 50)
    contraseña = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    #es_soporte = models.IntegerField
    #usuario_logueado = models.IntegerField


