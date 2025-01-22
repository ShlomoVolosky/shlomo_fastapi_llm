# app/schemas.py

from pydantic import BaseModel
from typing import List


class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 50
    num_return_sequences: int = 1


class GenerateResponse(BaseModel):
    results: List[str]


class EncodeRequest(BaseModel):
    text: str


class EncodeResponse(BaseModel):
    token_ids: List[int]


class DecodeRequest(BaseModel):
    token_ids: List[int]


class DecodeResponse(BaseModel):
    text: str
