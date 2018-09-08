from django.db import models

# Create your models here.
class Comentario(models.Model):
    ip = models.CharField(max_length=20)
    contenido = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.contenido