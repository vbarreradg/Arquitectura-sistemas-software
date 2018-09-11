from django.db import models

# Create your models here.
class Comentario(models.Model):
    ip = models.GenericIPAdressField()
    contenido = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.contenido
