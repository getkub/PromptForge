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

3. (Optional) For video generation capabilities:
   ```bash
   # Clone LTX-Video repository
   git clone https://github.com/Lightricks/LTX-Video ../Lightricks/LTX-Video
   ```

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

   # Generate a video (requires LTX-Video setup)
   ./run.sh config/prompts/video/examples/scene-generation-01.yaml
   ```

4. Launch the web interface (Optional):
   ```bash
   ./run_web.sh
   ```
   This starts a web server at http://localhost:8000 where you can:
   - Browse available example prompts
   - Run examples with the LLM
   - View formatted responses in a user-friendly interface
   - Generate videos (if LTX-Video is set up)

## Documentation

- [User Guide](docs/user-guide/README.md) - Basic usage and prompt system overview
- [Web Interface](docs/user-guide/web-gui.md) - Using the web-based GUI
- [Examples](docs/examples/README.md) - Example use cases and code samples
- [Working with Templates](docs/examples/working-with-templates.md) - Guide to creating and troubleshooting templates
- [Troubleshooting](docs/user-guide/troubleshooting.md) - Solutions for common issues
- [LTX-Video Integration](docs/ltx-video/README.md) - Guide to video generation capabilities

## Project Structure

- `src/llm_interface/`: Core Python modules
- `config/`: Configuration files and prompts
  - `prompts/`: Prompt templates and examples
    - `medical/examples/`: Medical diagnostics examples
    - `creative/examples/`: Creative writing examples
    - `business/examples/`: Business analysis examples
    - `technical/examples/`: Technical documentation examples
    - `video/examples/`: Video generation examples (requires LTX-Video)
- `docs/`: Detailed documentation
  - `ltx-video/`: Documentation for video generation features
- `tests/`: Test files
- `output/`: Directory where generated responses and videos are saved

## License

MIT
