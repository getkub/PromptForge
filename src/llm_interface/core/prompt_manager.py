"""
Module for managing and formatting prompts.
"""
import os
import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional

class PromptManager:
    def __init__(self, config_dir: str = "config/prompts"):
        self.config_dir = Path(config_dir)
        self._templates: Dict[str, Dict[str, Any]] = {}
        self._load_templates()
    
    def _load_templates(self) -> None:
        """Load all template files into memory."""
        for yaml_file in self.config_dir.rglob("*.yaml"):
            try:
                with open(yaml_file, "r") as f:
                    data = yaml.safe_load(f)
                    if "prompt_id" in data:
                        self._templates[data["prompt_id"]] = data
            except Exception as e:
                print(f"Error loading template {yaml_file}: {e}")
    
    def get_template(self, prompt_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a template by its ID.
        
        Args:
            prompt_id: The identifier for the prompt template
        
        Returns:
            Template data or None if not found
        """
        return self._templates.get(prompt_id)
    
    def format_prompt(self, prompt_id: str, **parameters: Dict[str, Any]) -> str:
        """
        Format a prompt template with the given parameters.
        
        Args:
            prompt_id: The identifier for the prompt template
            parameters: Key-value pairs for template parameters
        
        Returns:
            Formatted prompt string
        
        Raises:
            ValueError: If template not found or required parameters missing
        """
        template_data = self.get_template(prompt_id)
        if not template_data:
            raise ValueError(f"Template not found: {prompt_id}")
        
        template = template_data.get("template")
        if not template:
            raise ValueError(f"Template content not found in {prompt_id}")
        
        # Validate required parameters
        required_params = [
            name for name, param in template_data.get("parameters", {}).items()
            if param.get("required", False)
        ]
        missing_params = [param for param in required_params if param not in parameters]
        if missing_params:
            raise ValueError(f"Missing required parameters: {missing_params}")
        
        # Apply default values for missing optional parameters
        for param_name, param_info in template_data.get("parameters", {}).items():
            if param_name not in parameters and "default" in param_info:
                parameters[param_name] = param_info["default"]
        
        # Process array parameters to convert them to strings
        processed_params = {}
        for key, value in parameters.items():
            if isinstance(value, list):
                processed_params[key] = ", ".join(value)
            else:
                processed_params[key] = value
        
        try:
            # Log the parameters being used for formatting
            print(f"Formatting prompt with parameters: {processed_params}")
            return template.format(**processed_params)
        except KeyError as e:
            raise ValueError(f"Missing parameter in template: {e}")
        except Exception as e:
            raise ValueError(f"Error formatting template: {e}")
    
    def list_prompts(self, domain: str = None) -> List[Dict[str, Any]]:
        """
        List available prompts, optionally filtered by domain.
        
        Args:
            domain: Optional domain to filter prompts
        
        Returns:
            List of prompt metadata
        """
        prompts = []
        search_path = self.config_dir / domain if domain else self.config_dir
        
        for yaml_file in search_path.rglob("*.yaml"):
            try:
                with open(yaml_file, "r") as f:
                    data = yaml.safe_load(f)
                    prompts.append({
                        "id": data.get("prompt_id"),
                        "name": data.get("name"),
                        "description": data.get("description"),
                        "path": str(yaml_file)
                    })
            except Exception as e:
                print(f"Error loading {yaml_file}: {e}")
        
        return prompts 