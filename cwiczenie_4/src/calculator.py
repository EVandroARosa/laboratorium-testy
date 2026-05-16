class Calculator:
    """Kalkulator z historią operacji."""
    def __init__(self):
        self._history = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero.")
        result = a / b
        self._history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self) -> list:
        return list(self._history)