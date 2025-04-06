#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Get Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Using Python version: $PYTHON_VERSION"

# Remove existing virtual environment if it exists
if [ -d "venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

# Create new virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Ensure we're using the virtual environment's Python
VENV_PYTHON="$(pwd)/venv/bin/python3"
VENV_PIP="$(pwd)/venv/bin/pip3"

# Upgrade pip
echo "Upgrading pip..."
"$VENV_PYTHON" -m pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
"$VENV_PIP" install -r requirements.txt

# Create symlinks for python/python3 if they don't exist
if [ ! -L "venv/bin/python" ]; then
    ln -s python3 venv/bin/python
fi

echo "Setup complete! Virtual environment is activated."
echo "To activate the virtual environment in the future, run: source venv/bin/activate" 