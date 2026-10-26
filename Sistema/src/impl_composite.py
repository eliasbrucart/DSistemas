from Sistema.src.patterns.component import Component

class ImplCompoiste():
    def client_code1(self, component: Component) -> None:
        return f"RESULT: {component.operation()}"

    def client_code2(component1: Component, component2: Component) -> None:
        if component1.is_composite():
            component1.add(component2)

        return f"RESULT: {component1.operation()}"
