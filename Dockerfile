FROM python:3.12-slim
WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY README.md .
COPY src ./src

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD ["uvicorn", "arithmetic_calculator.main:app", "--host", "0.0.0.0", "--port", "8000"]
