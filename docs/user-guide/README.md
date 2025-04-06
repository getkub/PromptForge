# User Guide

## Table of Contents

1. [Basic Usage](basic-usage.md)
2. [Prompt System](prompt-system.md)
3. [Configuration](configuration.md)
4. [Advanced Usage](advanced-usage.md)

## Overview

The Local LLM Interface provides a structured way to interact with local language models. This guide will help you understand and use the system effectively.

## Quick Reference

### Running the Example

```bash
./run.sh
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

- Read [Basic Usage](basic-usage.md) to get started
- Explore the [Prompt System](prompt-system.md) to understand how prompts work
- Check [Configuration](configuration.md) for customization options
- See [Advanced Usage](advanced-usage.md) for more complex scenarios 