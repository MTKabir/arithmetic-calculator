from pydantic import BaseModel

class InputDTO(BaseModel):
    first_number: float
    second_number: float

class OutputDTO(BaseModel):
    result: float
