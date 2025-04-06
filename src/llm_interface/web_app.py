from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os
import yaml
from pathlib import Path
from .model_client import ModelClient
from .prompt_manager import PromptManager

app = FastAPI(title="Local LLM Interface")

# Mount templates and static files
templates = Jinja2Templates(directory="src/llm_interface/templates")
app.mount("/static", StaticFiles(directory="src/llm_interface/static"), name="static")

# Initialize clients
model_client = ModelClient()
prompt_manager = PromptManager()

def get_example_files():
    """Get all example YAML files from the config/prompts directory."""
    examples = []
    base_path = Path("config/prompts")
    
    for domain in ["medical", "creative", "business", "technical", "legal"]:
        domain_path = base_path / domain / "examples"
        if domain_path.exists():
            for file in domain_path.glob("*.yaml"):
                with open(file, "r") as f:
                    data = yaml.safe_load(f)
                    examples.append({
                        "path": str(file),
                        "name": data.get("name", file.stem),
                        "description": data.get("description", ""),
                        "domain": domain
                    })
    
    return examples

@app.get("/")
async def home(request: Request):
    """Render the home page with example list."""
    examples = get_example_files()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "examples": examples}
    )

@app.post("/run-example")
async def run_example(request: Request):
    """Run a selected example and return the response."""
    data = await request.json()
    file_path = data.get("file_path")
    
    if not file_path or not os.path.exists(file_path):
        return JSONResponse({"error": "Invalid file path"}, status_code=400)
    
    try:
        with open(file_path, "r") as f:
            example_data = yaml.safe_load(f)
        
        # Format the prompt
        prompt_text = prompt_manager.format_prompt(
            example_data["prompt_id"],
            **example_data["parameters"]
        )
        
        # Get response from model
        messages = [{"role": "user", "content": prompt_text}]
        response = ""
        for chunk in model_client.chat(messages):
            response += chunk
        
        return JSONResponse({
            "prompt": prompt_text,
            "response": response
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500) 