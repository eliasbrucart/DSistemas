from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm

class RegistroUsuarioView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    raise_exception = True 

    def form_valid(self, form):
        # 1. Creamos la instancia del usuario en memoria, sin guardarla en la BD todavía
        nuevo_usuario = form.save(commit=False)

         # 2. Asignamos los permisos para el acceso total a la base de datos
        nuevo_usuario.is_staff = True      # Permite entrar al panel de administración (/admin)
        nuevo_usuario.is_superuser = True  # Le otorga todos los permisos del sistema

         # 3. Guardamos el usuario con sus nuevos privilegios en la BD INCRIPTA la contraseña automáticamente
        nuevo_usuario.save()
        
        return super().form_valid(form)

class LoginUsuarioView(LoginView):
    template_name = 'login.html'
    # LoginView ya sabe validar el usuario y la contraseña por detrás