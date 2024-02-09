#converts data types from django models to python data types which are easier to handle

from rest_framework import serializers
from .models import Registro

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'