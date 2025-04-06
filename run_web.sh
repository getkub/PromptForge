#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install required packages if not already installed
pip install fastapi uvicorn jinja2 pyyaml requests

# Install the package in development mode
pip install -e .

# Run the FastAPI application
python -m llm_interface.web_app 