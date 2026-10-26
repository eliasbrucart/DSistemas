class Base():
    def __init__(self):
        pass

    def metodo_base(self):
        #Esto se carga en memoria al iniciar el programa.
        #variables que se almacenan en el stack de la memoria.
        numero = 10
        numero2 = 20
        if numero > numero2:
            return f"El número {numero} es mayor que {numero2}"
        else:
            return f"El número {numero} no es mayor que {numero2}"

    def metodo_base2(self, numero, numero2):
        #Se carga en memoria al ejecutar el metodo.
        #Las variables se utilizan solo al momento de ejecutar el metodo y se eliminan al terminar.
        if numero > numero2:
            return f"El número {numero} es mayor que {numero2}"
        else:
            return f"El número {numero} no es mayor que {numero2}"

    def metodo_base3(self):
        #descripcion de variables. En este caso no hay magic numbers.
        edad = 25
        edad_limite = 30
        if(edad > edad_limite):
            return "La persona es mayor de 30 años"
        else:
            return "La persona es menor de 30 años"


    def nmetodo_magic_base4(self):
        edad = 25
        #El 30 es lo que se llama magic number.
        if(edad > 30):
            return "La persona es mayor de 30 años"
        else:
            return "La persona es menor de 30 años"