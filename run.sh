#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if virtual environment exists, if not run setup
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "Virtual environment not found. Running setup..."
    "$SCRIPT_DIR/setup.sh"
fi

# Activate virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Install the package in development mode
pip install -e "$SCRIPT_DIR"

# Use the virtual environment's Python
VENV_PYTHON="$SCRIPT_DIR/venv/bin/python3"

# Run the Python script with all arguments passed to this script
"$VENV_PYTHON" "$SCRIPT_DIR/src/example.py" "$@"

# Deactivate virtual environment when done
deactivate 