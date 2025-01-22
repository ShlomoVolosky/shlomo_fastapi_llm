# LLM REST API
This project provides a REST API for interacting with the GPT-2 model using FastAPI.

## Features
- **Generate Text:** Create text based on input prompts.
- **Encode Text:** Convert text to token IDs.
- **Decode Text:** Convert token IDs back to text.

## Endpoints
- `POST /generate`: Generates text from a prompt.
- `POST /encode`: Encodes text into token IDs.
- `POST /decode`: Decodes token IDs into text.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

## Docker Setup and Troubleshooting
If you encounter an error where Docker fails to execute `RUN poetry lock` during the build process, follow these steps to resolve it:

1. First, build and run the Docker container:
   ```bash
   docker build -t your-image-name .
   docker run -it your-image-name /bin/bash
   ```

2. Once inside the container's bash shell, execute these commands in sequence:
   ```bash
   poetry lock
   poetry install
   poetry run uvicorn app.main:app
   ```

These commands will properly initialize the Poetry environment and start the FastAPI application within the Docker container. This approach resolves the Poetry lock file generation issues that can occur during the Docker build process.