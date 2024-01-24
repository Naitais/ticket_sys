from django.db import models

class ticket(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
