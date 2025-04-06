# User Guide

## Table of Contents

1. [Prompt System](prompt-system.md) - Understanding and using the prompt system

## Overview

The Local LLM Interface provides a structured way to interact with local language models. This guide will help you understand and use the system effectively.

## Quick Reference

### Running Examples

```bash
# Run a medical diagnostics example
./run.sh config/prompts/medical/examples/symptoms-cardiac-chest-pain-01.yaml

# Run a creative writing example
./run.sh config/prompts/creative/examples/story-sci-fi-space-01.yaml
```

### Basic Code Example

```python
from llm_interface.model_client import ModelClient
from llm_interface.prompt_manager import PromptManager

# Initialize
client = ModelClient()
prompt_manager = PromptManager()

# Use a prompt
prompt_text = prompt_manager.format_prompt(
    "creative.templates.story.scifi",
    genre_focus="space exploration",
    main_character="a quantum archaeologist"
)

# Get response
messages = [{"role": "user", "content": prompt_text}]
for chunk in client.chat(messages):
    print(chunk, end="", flush=True)
```

## Next Steps

- Read [Prompt System](prompt-system.md) to understand how prompts work
- Check the [Examples](../examples/README.md) section for practical use cases 