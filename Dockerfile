# Use the official Python 3.10 slim image as the base
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry using pip
RUN pip install --no-cache-dir poetry uvicorn fastapi transformers torch

# Configure Poetry to install dependencies globally (no virtual environments)
RUN poetry config virtualenvs.create false

# Copy only the dependency specification files to leverage Docker caching
COPY pyproject.toml poetry.lock /app/

# Verify Poetry installation
RUN poetry --version

# Copy the entire application code into the container
COPY . /app/

# (Optional) Expose port 8000 if your application listens on this port
EXPOSE 8000

# Define the default command to launch an interactive shell
CMD ["/bin/bash"]