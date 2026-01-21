class Calculator:

    def __init__(self, first_number: float, second_number: float):
        self._first_number = first_number
        self._second_number = second_number
        self._result = None

    def get_first_number(self) -> float:
        return self._first_number

    def get_second_number(self) -> float:
        return self._second_number

    def get_result(self):
        return self._result

    def set_first_number(self, value: float) -> None:
        self._first_number = value

    def set_second_number(self, value: float) -> None:
        self._second_number = value

    def set_result(self, value: float) -> None:
        self._result = value
