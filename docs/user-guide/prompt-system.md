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

## Troubleshooting Templates

### Common Template Issues

1. **Missing Parameters**
   
   Error: `Missing parameter in template: <parameter_name>`
   
   This occurs when a template references a parameter that isn't provided. To fix:
   
   - Ensure all parameters referenced in your template string are included in the example file
   - Check for typos in parameter names
   - Ensure the parameter is defined properly in both the template and example

2. **List Parameter Formatting**
   
   Arrays/lists in templates require special handling:
   
   - In template files, use `{parameter_name}` for list parameters - avoid direct operations like `{', '.join(parameter_name)}`
   - In example files, format lists properly as YAML arrays:
     ```yaml
     themes:
       - "theme one"
       - "theme two"
     ```
   - The system automatically converts lists to comma-separated strings during formatting

3. **Template Loading Issues**
   
   If templates aren't being found:
   
   - Ensure the `prompt_id` in the template matches the expected ID
   - Verify file paths follow the correct domain/subdomain structure
   - Check the file permissions are correct

### Debugging Templates

When developing new templates:

1. **Print the formatted prompt** before passing it to the model:
   ```python
   formatted_prompt = prompt_manager.format_prompt(example["prompt_id"], **example["parameters"])
   print(formatted_prompt)
   ```

2. **Log the parameters** being passed to format_prompt:
   ```python
   print(f"Parameters: {example['parameters']}")
   ```

3. **Test with minimal parameters** first, then add more complex ones

4. **Validate YAML syntax** in both template and example files 