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

# Run the Python script with all arguments passed to this script
python "$SCRIPT_DIR/src/example.py" "$@"

# Deactivate virtual environment when done
deactivate 