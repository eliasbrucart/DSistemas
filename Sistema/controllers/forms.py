from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models.models import UsersModel

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsersModel
        # Mostramos los campos solicitados en el formulario
        fields = ['first_name', 'last_name', 'username']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de Usuario',
        }