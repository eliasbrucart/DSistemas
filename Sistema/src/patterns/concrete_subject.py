from .subject import Subject
from .observer import Observer
from random import randrange

class ConcreteSubject(Subject):
    _state: int = None

    _observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        #print("Subject: Attached an observer.")
        self._observers.append(observer)
        return "Subject: Attached an observer."

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        #print("Subject: Notifying observers...")
        observer_response = ""
        for observer in self._observers:
            observer_response = observer.update(self)
        return f"Subject: Notifying observers... {observer_response}"


    def some_business_logic(self) -> None:
        self._state = randrange(0, 10)
        #print(f"Subject: My state has changed to {self._state}")
        response_notify = self.notify()
        return f"Subject: My state has changed to {self._state} " + response_notify