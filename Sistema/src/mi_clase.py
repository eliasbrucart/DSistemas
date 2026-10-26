from Sistema.src.base import Base
from Sistema.src.composicion import Composicion

class MiClase(Base): #Herencia de la clase Base
    def __init__(self):
        super().__init__()
        self.objeto_composicion = Composicion() #Composición de la clase Composicion

    def mi_metodo(self, mensaje):
        return mensaje

    def agregacion(self, objeto_agregacion):
        self.objeto_agregacion = objeto_agregacion #Agregación de la clase Agregacion
        return f"Objeto agregado - Nombre: {self.objeto_agregacion.nombre}, Apellido: {self.objeto_agregacion.apellido}"
    

    
