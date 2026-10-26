from django.shortcuts import render
#from Sistema.src.mi_clase import MiClase
#from Sistema.src.agregacion import Agregacion
from Sistema.Sistema.old_files.models import Prueba
from Sistema.src.base import Base
from Sistema.src.patterns.singleton import Singleton
#imports composite
from Sistema.src.patterns.composite import Composite
from Sistema.src.patterns.leaf import Leaf
from Sistema.src.impl_composite import ImplCompoiste
#import strategy
from Sistema.src.patterns.context import Context
from Sistema.src.patterns.strategy_a import StrategyA
from Sistema.src.patterns.strategy_b import StrategyB
#import observer
from Sistema.src.patterns.concrete_subject import ConcreteSubject
from Sistema.src.patterns.concrete_observer_a import ConcreteObserverA
from Sistema.src.patterns.concrete_observer_b import ConcreteObserverB


#Este archivo de view es un controller en django.
def index(request):   #request->GET,POST,PUT,DELETE
    instanciaBase = Base()
    respuesta_base = instanciaBase.metodo_base2(15, 10)

    instancia_singleton1 = Singleton()
    instancia_singleton2 = Singleton()

    respuesta_singleton = ""
    if id(instancia_singleton1) == id(instancia_singleton2):
        respuesta_singleton = "Las instancias del Singleton son iguales"
    else:
        respuesta_singleton = "Las instancias del Singleton son diferentes"


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


    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        descripcion = request.POST.get('descripcion')

        # Crear una nueva instancia del modelo Prueba y guardarla en la base de datos
        nueva_prueba = Prueba(nombre=nombre, apellido=apellido, descripcion=descripcion)
        nueva_prueba.save()

    return render(request, 'index.html', {'respuesta_base': respuesta_base, 'respuesta_singleton': respuesta_singleton, 'respuesta_simple': respuesta_simple, 'respuesta_tree': respuesta_tree, 'respuesta_strategy': respuesta_strategy, 'respuesta_strategyB': respuesta_strategyB, 'response_subject_a': response_subject_a, 'response_subject_b': response_subject_b, 'observer_a': observer_a, 'observer_b': observer_b})

