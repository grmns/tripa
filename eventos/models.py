from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes_eventos/', blank=True, null=True, verbose_name=_("Imagen"))

    def __str__(self):
        return self.nombre
