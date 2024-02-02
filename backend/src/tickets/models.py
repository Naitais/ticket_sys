from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
