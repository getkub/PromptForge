#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install required packages if not already installed
pip install fastapi uvicorn jinja2 pyyaml

# Install the package in development mode
pip install -e .

# Add the src directory to the Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)/src

# Run the FastAPI application
uvicorn llm_interface.web_app:app --reload --host 0.0.0.0 --port 8080 