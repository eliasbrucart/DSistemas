from .singleton_meta import SingletonMeta

class Singleton(metaclass=SingletonMeta):
    def my_logic(self):
        return "Lógica de mi clase"