import os
import yaml
from typing import Dict, Any, Optional, List
import json

class PromptManager:
    def __init__(self, prompts_dir: str = "config/prompts"):
        self.prompts_dir = prompts_dir
        self.prompts: Dict[str, Any] = {}
        self.schema = self._load_schema()
        self._load_prompts()

    def _load_schema(self) -> Dict[str, Any]:
        """Load the prompt schema definition."""
        schema_path = os.path.join(os.path.dirname(self.prompts_dir), "schema.yaml")
        if os.path.exists(schema_path):
            with open(schema_path, 'r') as f:
                return yaml.safe_load(f)
        return {}

    def _load_prompts(self) -> None:
        """Load all YAML files from the prompts directory structure."""
        if not os.path.exists(self.prompts_dir):
            os.makedirs(self.prompts_dir)
            return

        for root, _, files in os.walk(self.prompts_dir):
            for file in files:
                if file.endswith(('.yaml', '.yml')):
                    file_path = os.path.join(root, file)
                    # Create prompt ID from path structure
                    relative_path = os.path.relpath(file_path, self.prompts_dir)
                    prompt_id = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')
                    
                    try:
                        with open(file_path, 'r') as f:
                            self.prompts[prompt_id] = yaml.safe_load(f)
                    except Exception as e:
                        print(f"Error loading prompt {file_path}: {e}")

    def list_prompts(self, domain: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List available prompts, optionally filtered by domain.
        
        Args:
            domain: Optional domain to filter prompts
            
        Returns:
            List of prompt metadata
        """
        prompts = []
        for prompt_id, prompt in self.prompts.items():
            if domain and prompt.get('domain') != domain:
                continue
            prompts.append({
                'id': prompt_id,
                'name': prompt.get('name'),
                'description': prompt.get('description'),
                'domain': prompt.get('domain'),
                'subdomain': prompt.get('subdomain'),
                'version': prompt.get('version')
            })
        return prompts

    def get_prompt(self, prompt_id: str) -> Optional[Dict[str, Any]]:
        """Get a prompt by its ID."""
        return self.prompts.get(prompt_id)

    def format_prompt(self, prompt_id: str, **kwargs) -> Optional[str]:
        """
        Get and format a prompt with the given parameters.
        
        Args:
            prompt_id: ID of the prompt to retrieve (e.g., 'creative.templates.story.scifi')
            **kwargs: Parameters to format the prompt with
        
        Returns:
            Formatted prompt string or None if prompt not found
        """
        prompt = self.get_prompt(prompt_id)
        if not prompt:
            print(f"Prompt not found: {prompt_id}")
            return None

        # Validate required parameters
        required_params = [
            name for name, param in prompt.get('parameters', {}).items()
            if param.get('required', False)
        ]
        
        missing_params = [param for param in required_params if param not in kwargs]
        if missing_params:
            print(f"Missing required parameters for {prompt_id}: {missing_params}")
            return None

        # Apply default values for missing optional parameters
        for param_name, param_info in prompt.get('parameters', {}).items():
            if param_name not in kwargs and 'default' in param_info:
                kwargs[param_name] = param_info['default']

        # Format the template
        try:
            template = prompt.get('template', '')
            if isinstance(template, str):
                return template.format(**kwargs)
            else:
                print(f"Invalid template format in {prompt_id}")
                return None
        except KeyError as e:
            print(f"Missing parameter in template: {e}")
            return None
        except Exception as e:
            print(f"Error formatting prompt {prompt_id}: {e}")
            return None

    def validate_prompt(self, prompt: Dict[str, Any]) -> List[str]:
        """
        Validate a prompt against the schema.
        
        Args:
            prompt: Prompt dictionary to validate
            
        Returns:
            List of validation errors, empty if valid
        """
        errors = []
        schema = self.schema.get('prompt_schema', {})
        
        # Check required fields
        for field in schema.get('required', []):
            if field not in prompt:
                errors.append(f"Missing required field: {field}")
        
        # Validate field types and values
        for field, value in prompt.items():
            if field in schema.get('properties', {}):
                field_schema = schema['properties'][field]
                if 'type' in field_schema:
                    expected_type = field_schema['type']
                    if expected_type == 'string' and not isinstance(value, str):
                        errors.append(f"Field {field} must be a string")
                    elif expected_type == 'object' and not isinstance(value, dict):
                        errors.append(f"Field {field} must be an object")
                    elif expected_type == 'array' and not isinstance(value, list):
                        errors.append(f"Field {field} must be an array")
        
        return errors 