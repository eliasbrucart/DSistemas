from django.contrib.auth.models import AbstractUser

class UsersModel(AbstractUser):
    # AbstractUser ya incluye de forma nativa:
    # first_name (Nombre), last_name (Apellido), username (Usuario) y password (Contraseña)
    
    def __str__(self):
        return self.username