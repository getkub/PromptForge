# Working with Templates

This guide demonstrates how to work with templates effectively, especially when handling list parameters and other complex structures.

## Basic Template Structure

Templates are defined in YAML files and include placeholders for parameters. Here's a basic template example:

```yaml
name: "template_name"
description: "Template description"
prompt_id: "domain.templates.type.name"
template: |
  This is a template with {parameter1} and {parameter2}.
  
  Multiple lines can be included using the YAML pipe character (|).
```

## Handling List Parameters

List parameters require special consideration in both templates and example files.

### Template Definition

When defining a template that accepts a list parameter:

```yaml
# config/prompts/creative/templates/story.fantasy.yaml
name: "fantasy_story_generator"
description: "Generates creative fantasy stories with customizable parameters"
prompt_id: "creative.templates.story.fantasy"
template: |
  You are a creative fantasy story writer. Create a {word_count}-word fantasy story with the following parameters:

  Genre Focus: {genre_focus}
  Main Character: {main_character}
  Setting: {setting}
  Time Period: {time_period}
  Context: {context}
  Themes: {themes}

  The story should be engaging, descriptive, and incorporate all the specified elements.
```

### Example File Definition

When providing list parameters in an example file:

```yaml
# config/prompts/creative/examples/story-fantasy-quest-01.yaml
name: "fantasy_story_generation"
description: "Example of a fantasy story with magical elements and a quest theme"
prompt_id: "creative.templates.story.fantasy"
parameters:
  genre_focus: "high fantasy"
  main_character: "a young elven mage apprentice"
  setting: "an ancient magical forest with hidden portals"
  time_period: "age of magic"
  word_count: 500
  context: "A magical artifact has been stolen from the elven council"
  themes: 
    - "coming of age"
    - "friendship"
    - "responsibility"
    - "magical discovery"
```

## Common Pitfalls and Solutions

### Avoid Template String Operations

❌ **Incorrect approach**:
```yaml
template: |
  Themes: {', '.join(themes)}
```

✅ **Correct approach**:
```yaml
template: |
  Themes: {themes}
```

The system will automatically handle the conversion of list parameters to comma-separated strings.

### Proper Indentation in YAML Files

Ensure proper indentation in your YAML files to avoid parsing errors:

```yaml
parameters:
  themes:  # Two spaces indentation
    - "first theme"  # Four spaces indentation
    - "second theme"
```

### Testing Your Templates

To test your templates before using them with a model:

```python
from llm_interface.core.prompt_manager import PromptManager

# Initialize the prompt manager
manager = PromptManager()

# Load and test a template
template_id = "creative.templates.story.fantasy"
parameters = {
    "genre_focus": "high fantasy",
    "main_character": "a wizard",
    "setting": "magical kingdom",
    "time_period": "medieval era",
    "word_count": 500,
    "context": "A dark force threatens the kingdom",
    "themes": ["magic", "friendship", "courage"]
}

# Format the prompt
formatted_prompt = manager.format_prompt(template_id, **parameters)
print(formatted_prompt)
```

## Summary

When working with templates that include list parameters:

1. Use simple placeholders like `{parameter_name}` in templates
2. Define lists properly indented in YAML example files
3. The system will automatically convert lists to comma-separated strings
4. Test your templates with minimal parameters first, then add complexity 