"""
API routes and handlers.
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from ..core.model_client import ModelClient
from ..core.prompt_manager import PromptManager
from ..services.example_service import ExampleService
from . import models

router = APIRouter()
example_service = ExampleService()

@router.get("/examples", response_model=List[models.Example])
async def list_examples():
    """List all available examples."""
    return example_service.list_examples()

@router.post("/run-example", response_model=models.ExampleResponse)
async def run_example(request: models.ExampleRequest):
    """Run a selected example."""
    try:
        return await example_service.run_example(request.file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 