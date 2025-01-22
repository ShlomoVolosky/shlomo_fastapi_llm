# app/main.py

from fastapi import FastAPI, HTTPException
from transformers import pipeline, set_seed
from app.schemas import GenerateRequest, GenerateResponse, EncodeRequest, EncodeResponse, DecodeRequest, DecodeResponse
from app.models import tokenizer, model

app = FastAPI(title="LLM REST API", description="An API for GPT-2 operations")

# Set seed for reproducibility
set_seed(42)

# Pipeline for text generation
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)


@app.post("/generate", response_model=GenerateResponse)
async def generate_text(request: GenerateRequest):
    """
    Generate text using the GPT-2 model.
    """
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    results = generator(
        request.prompt,
        max_length=request.max_length,
        num_return_sequences=request.num_return_sequences,
    )
    return {"results": [r["generated_text"] for r in results]}


@app.post("/encode", response_model=EncodeResponse)
async def encode_text(request: EncodeRequest):
    """
    Encode input text into token IDs using GPT-2 tokenizer.
    """
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    token_ids = tokenizer.encode(request.text)
    return {"token_ids": token_ids}


@app.post("/decode", response_model=DecodeResponse)
async def decode_text(request: DecodeRequest):
    """
    Decode token IDs into text using GPT-2 tokenizer.
    """
    if not request.token_ids:
        raise HTTPException(status_code=400, detail="Token IDs cannot be empty.")
    text = tokenizer.decode(request.token_ids)
    return {"text": text}
