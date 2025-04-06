# Local LLM Interface

A modular Python interface for interacting with local language models with a structured prompt management system.

## Prerequisites

1. Install [Ollama](https://ollama.ai/download) on your system
   ```bash
   # For macOS using Homebrew
   brew install ollama
   ```
2. Pull and serve a compatible model (e.g., Gemma 3:27b):
   ```bash
   # Pull the model
   ollama pull gemma:3b-27b

   # Run the model server
   ollama run gemma:3b-27b
   ```
   Note: The model server must be running before using this interface.

## Quick Start

1. Ensure Python 3 is installed on your system
2. Run the setup script:
   ```bash
   ./setup.sh
   ```
3. Run an example:
   ```bash
   # Run a medical diagnostics example
   ./run.sh config/prompts/medical/examples/symptoms-cardiac-chest-pain-01.yaml

   # Run a creative writing example
   ./run.sh config/prompts/creative/examples/story-sci-fi-space-01.yaml
   ```

## Documentation

- [User Guide](docs/user-guide/README.md) - Basic usage and prompt system overview
- [Examples](docs/examples/README.md) - Example use cases and code samples

## Project Structure

- `src/llm_interface/`: Core Python modules
- `config/`: Configuration files and prompts
  - `prompts/`: Prompt templates and examples
    - `medical/examples/`: Medical diagnostics examples (e.g., `symptoms-cardiac-chest-pain-01.yaml`)
    - `creative/examples/`: Creative writing examples (e.g., `story-sci-fi-space-01.yaml`)
    - `business/examples/`: Business analysis examples (e.g., `finance-retail-performance-01.yaml`)
    - `technical/examples/`: Technical documentation examples (e.g., `api-rest-documentation-01.yaml`)
- `docs/`: Detailed documentation
- `tests/`: Test files
- `output/`: Directory where generated responses are saved

## License

MIT
