# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/local-llm-interface.git
   cd local-llm-interface
   ```

2. Run the setup script:
   ```bash
   ./setup.sh
   ```
   This will:
   - Create a virtual environment
   - Install required dependencies
   - Set up Python version consistency

3. Verify the installation:
   ```bash
   ./run.sh
   ```

## Manual Installation

If you prefer to set up manually:

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Ensure your local model server is running (e.g., Ollama)
2. Default configuration assumes the model server is running at `http://localhost:11434`
3. To use a different server, modify the `base_url` in your code:
   ```python
   client = ModelClient(base_url="http://your-server:port")
   ```

## Troubleshooting

### Common Issues

1. **Virtual Environment Issues**
   - If you see "command not found: python", ensure Python is in your PATH
   - If venv creation fails, try: `python3 -m venv venv`

2. **Dependency Issues**
   - If pip install fails, try: `pip install --upgrade pip`
   - For specific package issues, check the package's documentation

3. **Model Server Connection**
   - Ensure your model server is running
   - Check the server URL in your configuration
   - Verify network connectivity and firewall settings

### Getting Help

- Check the [User Guide](../user-guide/README.md) for detailed usage instructions
- Visit the [API Reference](../api-reference/README.md) for technical details
- Review [Examples](../examples/README.md) for common use cases 