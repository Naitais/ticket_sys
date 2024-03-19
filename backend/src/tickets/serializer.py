#converts data types from django models to python data types which are easier to handle

from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='ticket-highlight', format='html')

    #Our snippet and user serializers include 'url' fields that by default will refer to '{model_name}-detail', which in this case
    #al usar hyperlinkedmodelserializer, automaticamente incluye al campo url que automaticamente apunte a '{model_name}-detail' por eso
    #no puedo cambiarle el nombre a como llamo la url del detalle que apunta  ala vista detalle

    class Meta:
        model = Ticket
        fields = ['url','id_ticket','highlight', 'fecha_creacion', 'usuario', 'concepto', 'empresa', 
                  'agente_legajo', 'agente_nombre', 'observaciones', 'estado_ticket','devoluciones']