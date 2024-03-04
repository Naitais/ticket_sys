from django.db import models
import datetime
import getpass

username = getpass.getuser()

class Registro(models.Model):
    id_registro = models.AutoField(primary_key=True)
    fecha_liquidaciones = models.TextField(default = datetime.date.today)
    operador_liquidaciones = models.CharField(max_length=100, default= username)
    concepto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    legajo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    observaciones = models.TextField(default = ' ')
    estado_liquidaciones = models.CharField(max_length=50, default = ' ')
    operador_sistemas = models.CharField(max_length=100, default = ' ')
    estado_sistemas = models.CharField(max_length=50, default = ' ')
    devoluciones = models.TextField(default = ' ')
    fecha_sistemas = models.TextField(default = ' ')

