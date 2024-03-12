from django.contrib import admin

from .models import Usuario, Ticket

admin.site.register(Ticket)
admin.site.register(Usuario)

# Register your models here.
