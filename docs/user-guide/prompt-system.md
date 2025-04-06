# Prompt System

## Overview

The prompt system provides a structured way to manage and use prompts with local language models. It uses a hierarchical organization and a standardized schema for consistency and validation.

## Prompt IDs

Prompts are identified by their hierarchical path in the configuration directory:

```
domain.subdomain.template_name
```

Examples:
- `creative.templates.story.scifi`: Science fiction story generator
- `medical.templates.diagnostics.symptoms`: Medical symptom analysis

## Prompt Schema

Each prompt follows a standardized schema defined in `config/schema.yaml`:

```yaml
name: "unique_identifier"
description: "Detailed description"
version: "1.0"
domain: "primary_domain"
subdomain: "specific_use_case"
author: "Author or Team"

template: |
  The actual prompt template with {parameters}

parameters:
  parameter_name:
    type: string|integer|float|boolean|array
    description: "Parameter description"
    default: "default_value"
    required: true|false

metadata:
  tags: ["tag1", "tag2"]
  use_cases: ["use case 1", "use case 2"]
  examples:
    - input: {parameter_values}
      expected_output: "Example output"
```

## Directory Structure

```
config/
├── schema.yaml                    # Schema definition
└── prompts/
    ├── creative/
    │   └── templates/
    │       └── story.scifi.yaml   # Sci-fi story template
    ├── medical/
    │   └── templates/
    │       └── diagnostics.symptoms.yaml  # Medical diagnostics template
    ├── business/
    │   └── templates/
    └── technical/
        └── templates/
```

## Using Prompts in Code

```python
from llm_interface.prompt_manager import PromptManager

# Initialize the prompt manager
prompt_manager = PromptManager()

# List available prompts
for prompt in prompt_manager.list_prompts():
    print(f"- {prompt['id']}: {prompt['name']}")
    print(f"  Description: {prompt['description']}")
    print(f"  Domain: {prompt['domain']}.{prompt['subdomain']}")

# Use a specific prompt
prompt_id = "creative.templates.story.scifi"
prompt_params = {
    "genre_focus": "space exploration",
    "main_character": "a quantum archaeologist",
    "setting": "ancient alien ruins",
    "time_period": "year 2250",
    "word_count": 400,
    "themes": ["discovery", "ancient mysteries"]
}

# Format the prompt with parameters
prompt_text = prompt_manager.format_prompt(prompt_id, **prompt_params)
```

## Adding New Prompts

1. Create a new YAML file in the appropriate domain directory:
   ```
   config/prompts/domain/subdomain/template_name.yaml
   ```

2. Follow the schema defined in `config/schema.yaml`

3. Include required fields:
   - `name`: Unique identifier
   - `description`: What the prompt does
   - `template`: The actual prompt template
   - `parameters`: Parameters that can be used in the template

4. Add metadata:
   - `tags`: Keywords for categorization
   - `use_cases`: Specific use cases
   - `examples`: Example inputs and outputs

## Best Practices

1. **Naming Conventions**
   - Use lowercase for file names
   - Use dots to separate components in the prompt ID
   - Be descriptive but concise

2. **Parameter Design**
   - Make parameters reusable across similar prompts
   - Provide meaningful default values
   - Document parameter constraints

3. **Template Structure**
   - Use clear section headers
   - Include examples in the template
   - Format for readability

4. **Metadata**
   - Add relevant tags for searchability
   - Include diverse examples
   - Document use cases thoroughly 