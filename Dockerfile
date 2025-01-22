# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry install --no-dev

COPY app /app/app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
