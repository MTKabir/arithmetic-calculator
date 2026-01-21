from fastapi import APIRouter
from arithmetic_calculator.api.calculator_routes import router as calculator_router

router = APIRouter(prefix="/api")

router.include_router(calculator_router)
