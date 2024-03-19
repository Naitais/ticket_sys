#converts data types from django models to python data types which are easier to handle

from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id_ticket', 'fecha_creacion', 'usuario', 'concepto', 'empresa', 
                  'agente_legajo', 'agente_nombre', 'observaciones', 'estado_ticket','devoluciones']
