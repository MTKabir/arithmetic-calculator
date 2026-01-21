from fastapi import FastAPI
from arithmetic_calculator.api.v1 import router as v1

app = FastAPI(title="Arithmetic Calculator API")

app.include_router(v1)