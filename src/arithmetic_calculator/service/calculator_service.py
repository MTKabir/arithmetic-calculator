from arithmetic_calculator.repository.calculator_repository import CalculatorRepository
from arithmetic_calculator.dto.calculator_dto import InputDTO, OutputDTO
from src.arithmetic_calculator.dto.calculator_dto import HistoryResponseDTO

class CalculatorService:
    def __init__(self, repository: CalculatorRepository ):
        self.repository = repository

    def validate_user_input(self, a, b) -> bool:
        return isinstance(a, (int, float)) and isinstance(b, (int, float))

    def addition(self, dto: InputDTO) -> OutputDTO:
            result = dto.first_number + dto.second_number
            self.repository.save({
                "operation": "add",
                "first_number": dto.first_number,
                "second_number": dto.second_number,
                "result": result
            })
            return OutputDTO(result=result)

    def subtraction(self, dto: InputDTO) -> OutputDTO:
        result = dto.first_number - dto.second_number
        self.repository.save({
            "operation": "subtract",
            "first_number": dto.first_number,
            "second_number": dto.second_number,
            "result": result
        })
        return OutputDTO(result=result)

    def multiplication(self, dto: InputDTO) -> OutputDTO:
        result = dto.first_number * dto.second_number
        self.repository.save({
            "operation": "multiply",
            "first_number": dto.first_number,
            "second_number": dto.second_number,
            "result": result
        })
        return OutputDTO(result=result)
    
    def division(self, dto: InputDTO) -> OutputDTO:
        result = dto.first_number / dto.second_number
        self.repository.save({
            "operation": "divide",
            "first_number": dto.first_number,
            "second_number": dto.second_number,
            "result": result
        })
        return OutputDTO(result=result)

    def history(self) -> HistoryResponseDTO:
        history = self.repository.find_all()
        return HistoryResponseDTO(history=history)