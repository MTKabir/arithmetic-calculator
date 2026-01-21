from fastapi import APIRouter
from arithmetic_calculator.dto.calculator_dto import HistoryResponseDTO, InputDTO, OutputDTO
from arithmetic_calculator.service.calculator_service import CalculatorService
from arithmetic_calculator.repository.calculator_repository import CalculatorRepository

router = APIRouter(prefix="/calculator", tags=["Calculator"])

repository = CalculatorRepository()
service = CalculatorService(repository)

@router.post("/addition", response_model=OutputDTO)
def add_numbers(request: InputDTO):
    return service.addition(request)

@router.post("/subtraction", response_model=OutputDTO)
def subtract_numbers(request: InputDTO):
    return service.subtraction(request)

@router.post("/multiplication", response_model=OutputDTO)
def multiply_numbers(request: InputDTO):
    return service.multiplication(request)

@router.post("/division", response_model=OutputDTO)
def divide_numbers(request: InputDTO):
    return service.division(request)

@router.get("/history", response_model=HistoryResponseDTO)
def get_history():
    return service.history()



