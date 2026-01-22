import pytest
from arithmetic_calculator.service.calculator_service import CalculatorService
from arithmetic_calculator.dto.calculator_dto import InputDTO
from arithmetic_calculator.repository.calculator_repository import CalculatorRepository

@pytest.fixture
def service():
    repository = CalculatorRepository()
    return CalculatorService(repository)

def test_addition(service):
    dto = InputDTO(first_number=2, second_number=3)
    result = service.addition(dto)
    assert result.result == 5

def test_subtraction(service):
    dto = InputDTO(first_number=5, second_number=2)
    result = service.subtraction(dto)
    assert result.result == 3


def test_multiplication(service):
    dto = InputDTO(first_number=4, second_number=3)
    result = service.multiplication(dto)
    assert result.result == 12


def test_division(service):
    dto = InputDTO(first_number=10, second_number=2)
    result = service.division(dto)
    assert result.result == 5


def test_history(service):
    service.addition(InputDTO(first_number=1, second_number=2))
    service.subtraction(InputDTO(first_number=5, second_number=3))
    history_response = service.history()
    assert len(history_response.history) == 2
    assert history_response.history[0].operation == "add"
    assert history_response.history[1].operation == "subtract"
