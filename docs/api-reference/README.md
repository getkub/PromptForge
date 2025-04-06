# API Reference

## Table of Contents

1. [ModelClient](model-client.md) - API for interacting with language models
2. [PromptManager](prompt-manager.md) - API for managing prompts
3. [Configuration](configuration.md) - Configuration options

## Overview

This section provides detailed technical documentation for the Local LLM Interface API. Each component is documented with its methods, parameters, and usage examples.

## Quick Reference

### ModelClient

```python
from llm_interface.model_client import ModelClient

# Initialize with default settings
client = ModelClient()  # Uses http://localhost:11434

# Initialize with custom settings
client = ModelClient(base_url="http://your-server:port")

# Send a chat request
messages = [{"role": "user", "content": "Hello"}]
for chunk in client.chat(messages, model="gemma3:27b", stream=True):
    print(chunk, end="", flush=True)
```

### PromptManager

```python
from llm_interface.prompt_manager import PromptManager

# Initialize
prompt_manager = PromptManager()

# List available prompts
prompts = prompt_manager.list_prompts(domain="creative")

# Format a prompt
prompt_text = prompt_manager.format_prompt(
    "creative.templates.story.scifi",
    genre_focus="space exploration"
)
```

## Next Steps

- Read [ModelClient](model-client.md) for detailed API documentation
- Check [PromptManager](prompt-manager.md) for prompt management features
- See [Configuration](configuration.md) for customization options 