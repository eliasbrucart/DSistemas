from urllib.parse import urljoin

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.views import View

from ..models.prueba_model import Prueba
from ..src.base import Base
from ..src.patterns.singleton import Singleton
#imports composite
from ..src.patterns.composite import Composite
from ..src.patterns.leaf import Leaf
from ..src.impl_composite import ImplCompoiste
#import strategy
from ..src.patterns.context import Context
from ..src.patterns.strategy_a import StrategyA
from ..src.patterns.strategy_b import StrategyB
#import observer
from ..src.patterns.concrete_subject import ConcreteSubject
from ..src.patterns.concrete_observer_a import ConcreteObserverA
from ..src.patterns.concrete_observer_b import ConcreteObserverB
#import logging para registrar eventos
import logging

from ..src.services import obtener_datos_api

import os
from dotenv import load_dotenv #pip install dotenv
from pathlib import Path

logging.basicConfig(
    filename='events.log',  # Nombre o ruta del archivo
    filemode='a',                  # 'a' para añadir texto, 'w' para sobrescribir el archivo cada vez
    level=logging.DEBUG,           # Nivel mínimo de eventos que se registrarán
    format='%(asctime)s - %(levelname)s - %(message)s', # Estructura del mensaje
    datefmt='%Y-%m-%d %H:%M:%S'    # Formato de la fecha y hora
)



class IndexView(View):
    def renderIndex(self, request):
        load_dotenv(Path(__file__).resolve().parents[1] / ".env")

        ENDPOINT_API = os.getenv("ENDPOINT_API")
        if not ENDPOINT_API:
            raise ImproperlyConfigured("ENDPOINT_API no está definida en el entorno.")

        instanciaBase = Base()
        respuesta_base = instanciaBase.metodo_base2(15, 10)
        
        instancia_singleton1 = Singleton()
        instancia_singleton2 = Singleton()
        
        respuesta_singleton = ""
        if id(instancia_singleton1) == id(instancia_singleton2):
            respuesta_singleton = "Las instancias del Singleton son iguales"
            logging.warning("Se ejecuto mal el singleton")
        else:
            respuesta_singleton = "Las instancias del Singleton son diferentes"
            logging.debug("Se ejecuto bien el singleton")
        
        
        impl_composite = ImplCompoiste()
        
        simple = Leaf()
        respuesta_simple = impl_composite.client_code1(simple)
        
        tree = Composite() #arbol principal
        
        branch1 = Composite() #rama1 de nuestro arbol
        branch1.add(Leaf()) #a la rama 1 le agregamos una hoja
        branch1.add(Leaf()) #a la rama 1 le agregamos una hoja
        
        branch2 = Composite() #rama2 de nuestro arbol
        branch2.add(Leaf()) #a la rama 2 le agregamos una hoja
        
        tree.add(branch1) #argremos la rama 1 al arbol principal
        tree.add(branch2) #argremos la rama 2 al arbol principal
        
        respuesta_tree = impl_composite.client_code1(tree)
        
        #respuesta_tree_simple = impl_composite.client_code2(tree, simple)
        
        #implementacion de strategy
        context = Context(StrategyA())
        respuesta_strategy = context.do_some_business_logic()
        
        context.strategy = StrategyB()
        respuesta_strategyB = context.do_some_business_logic()
        
        subject = ConcreteSubject()
        observer_a = ConcreteObserverA()
        subject.attach(observer_a)
        response_subject_a = subject.some_business_logic()
        
        observer_b = ConcreteObserverB()
        subject.attach(observer_b)
        response_subject_b = subject.some_business_logic()

        url_api = f"{ENDPOINT_API}products/?limit=10"
        #url_api = urljoin(ENDPOINT_API, "products/") + "?limit=10"
        datos = obtener_datos_api(url_api)
        contexto = {
            'elementos': datos
        }

        return render(request, 'index.html', {'respuesta_base': respuesta_base, 'respuesta_singleton': respuesta_singleton, 'respuesta_simple': respuesta_simple, 'respuesta_tree': respuesta_tree, 'respuesta_strategy': respuesta_strategy, 'respuesta_strategyB': respuesta_strategyB, 'response_subject_a': response_subject_a, 'response_subject_b': response_subject_b, 'observer_a': observer_a, 'observer_b': observer_b, 'contexto': contexto})

    def postFormData(self, request):
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            descripcion = request.POST.get('descripcion')
                
            # Crear una nueva instancia del modelo Prueba y guardarla en la base de datos
            nueva_prueba = Prueba(nombre=nombre, apellido=apellido, descripcion=descripcion)
            nueva_prueba.save()
            logging.debug(f"Se registraron nuevos datos en el formulario base: nombre: {nombre}, apellido: {apellido}, descripcion: {descripcion}")
            return render(request, 'index.html', {'mensajeFormData': 'Datos guardados correctamente'})
        return render(request, 'index.html')
    
    def post(self, request):
        return self.postFormData(request)

    def get(self, request):
        return self.renderIndex(request)