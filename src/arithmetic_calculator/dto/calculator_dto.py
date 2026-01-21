from typing import List
from pydantic import BaseModel

class InputDTO(BaseModel):
    first_number: float
    second_number: float

class OutputDTO(BaseModel):
    result: float

class HistoryDTO(BaseModel):
    operation: str
    first_number: float
    second_number: float
    result: float
class HistoryResponseDTO(BaseModel):
    history: List[HistoryDTO]