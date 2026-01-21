class CalculatorRepository:
    def __init__(self):
        self._history = []

    def save(self, calculation: dict) -> None:
        self._history.append(calculation)

    def find_all(self):
        return self._history.copy()
