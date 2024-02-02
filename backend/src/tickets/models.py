from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

class Prueba(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
