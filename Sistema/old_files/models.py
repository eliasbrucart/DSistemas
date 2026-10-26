from django.db import models

from django.contrib.auth.models import AbstractUser

class Prueba(models.Model):
    nombre = models.CharField(max_length=255)

    apellido = models.CharField(max_length=255)

    descripcion = models.TextField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    

#class UsersModel(AbstractUser):
    # AbstractUser ya incluye de forma nativa:
    # first_name (Nombre), last_name (Apellido), username (Usuario) y password (Contraseña)
    
    #def __str__(self):
        #return self.username