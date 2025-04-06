# Local LLM Interface

A modular Python interface for interacting with local language models with a structured prompt management system.

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

- [Getting Started](docs/getting-started/installation.md) - Installation and basic setup
- [User Guide](docs/user-guide/README.md) - How to use the system
- [API Reference](docs/api-reference/README.md) - Detailed API documentation
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
