# Examples

## Table of Contents

1. [Basic Examples](basic.md) - Simple usage examples
2. [Creative Writing](creative-writing.md) - Story generation examples
3. [Medical Diagnostics](medical-diagnostics.md) - Medical analysis examples
4. [Advanced Usage](advanced.md) - Complex scenarios

## Overview

This section provides practical examples of using the Local LLM Interface for various use cases. Each example is stored as a YAML file in the appropriate domain directory.

## Example Naming Convention

Examples follow a structured naming convention:
```
{category}-{subcategory}-{sequence}.yaml
```

Where:
- `category`: The primary category (e.g., symptoms, story, finance, api)
- `subcategory`: The specific subcategory (e.g., cardiac-chest-pain, sci-fi-space, retail-performance)
- `sequence`: A sequential number (01, 02, etc.)

Examples:
- `symptoms-cardiac-chest-pain-01.yaml`: Cardiac symptoms analysis example
- `story-sci-fi-space-01.yaml`: Science fiction story generation example
- `finance-retail-performance-01.yaml`: Retail financial performance analysis example
- `api-rest-documentation-01.yaml`: REST API documentation generation example

## Running Examples

To run an example, use the `run.sh` script with the path to the example YAML file:

```bash
# Run a medical diagnostics example
./run.sh config/prompts/medical/examples/symptoms-cardiac-chest-pain-01.yaml

# Run a creative writing example
./run.sh config/prompts/creative/examples/story-sci-fi-space-01.yaml

# Run a business analysis example
./run.sh config/prompts/business/examples/finance-retail-performance-01.yaml

# Run a technical documentation example
./run.sh config/prompts/technical/examples/api-rest-documentation-01.yaml
```

The script will:
1. Load the example parameters from the YAML file
2. Use the specified prompt template
3. Generate a response
4. Save both the response and the prompt used to the `output` directory

## Example Structure

Each example YAML file contains:
```yaml
name: "example_name"
description: "Description of what the example demonstrates"
prompt_id: "domain.templates.type.name"
parameters:
  # Parameters specific to the prompt template
  param1: value1
  param2: value2
```

## Available Examples

### Medical Diagnostics
- `symptoms-cardiac-chest-pain-01.yaml`: Cardiac symptoms analysis for a 45-year-old female patient
- `symptoms-respiratory-copd-01.yaml`: Respiratory symptoms analysis for a 62-year-old male patient with COPD

### Creative Writing
- `story-sci-fi-space-01.yaml`: Space exploration story with quantum archaeology theme
- `story-fantasy-quest-01.yaml`: Fantasy story with magical elements and a quest theme

### Business Analysis
- `marketing-saas-campaign-01.yaml`: Marketing campaign analysis for a SaaS startup
- `finance-retail-performance-01.yaml`: Financial performance analysis for a retail company

### Technical Documentation
- `api-rest-documentation-01.yaml`: API documentation generation for a RESTful service
- `architecture-microservices-ecommerce-01.yaml`: Microservices architecture documentation for an e-commerce platform

## Next Steps

- Check [Basic Examples](basic.md) for more simple use cases
- Explore [Creative Writing](creative-writing.md) for story generation
- See [Medical Diagnostics](medical-diagnostics.md) for medical analysis
- Review [Advanced Usage](advanced.md) for complex scenarios 