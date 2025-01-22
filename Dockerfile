FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    cargo \ 
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Configure Poetry to avoid virtual environments
RUN poetry config virtualenvs.create false

# Copy project files
COPY pyproject.toml poetry.lock /app/

# Verify Poetry installation
RUN poetry --version

# Start a shell instead of running poetry install
CMD ["/bin/bash"]
