"""
API data models and schemas.
"""
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ExampleRequest(BaseModel):
    file_path: str

class ExampleResponse(BaseModel):
    prompt: str
    response: str

class ErrorResponse(BaseModel):
    error: str

class Example(BaseModel):
    path: str
    name: str
    description: str
    domain: str 