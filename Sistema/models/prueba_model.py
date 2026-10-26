from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

class Prueba(models.Model):
    nombre = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'Solo se permiten letras.')])

    apellido = models.CharField(max_length=255)

    descripcion = models.TextField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    