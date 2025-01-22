FROM python:3.10-slim 

WORKDIR /app 

# Install system dependencies 
RUN apt-get update && apt-get install -y --no-install-recommends \ 
    build-essential \ 
    libssl-dev \ 
    libffi-dev \ 
    python3-dev \ 
    && rm -rf /var/lib/apt/lists/* 

# Install Poetry 
RUN pip install poetry==2.0.1

# Configure Poetry to avoid virtual environments 
RUN poetry cache clear . --all

# Copy dependency files
COPY pyproject.toml poetry.lock /app/

# Debug step to verify files
RUN ls -la /app/


# Install Python dependencies 
RUN poetry install

# Copy application code 
COPY app /app/app 

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]