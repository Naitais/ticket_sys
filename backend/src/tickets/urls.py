from django.urls import path
from .views import index, nuevo_ticket

urlpatterns = [
    path('tickets/', index, name="index"),
    path('nuevo-ticket/', nuevo_ticket, name="nuevo-ticket"),
]