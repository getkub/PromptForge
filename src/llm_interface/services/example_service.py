"""
Service layer for handling example-related operations.
"""
import yaml
from typing import List, Dict, Any
from ..core.model_client import ModelClient
from ..core.prompt_manager import PromptManager

class ExampleService:
    def __init__(self):
        self.model_client = ModelClient()
        self.prompt_manager = PromptManager()
    
    def list_examples(self) -> List[Dict[str, Any]]:
        """
        List all available examples.
        
        Returns:
            List of example metadata
        """
        return self.prompt_manager.list_prompts()
    
    async def run_example(self, file_path: str) -> Dict[str, str]:
        """
        Run a specific example.
        
        Args:
            file_path: Path to the example YAML file
        
        Returns:
            Dictionary containing prompt and response
        """
        # Load example data
        with open(file_path, "r") as f:
            example_data = yaml.safe_load(f)
        
        # Format the prompt
        prompt_text = self.prompt_manager.format_prompt(
            example_data["prompt_id"],
            **example_data["parameters"]
        )
        
        # Get response from model
        messages = [{"role": "user", "content": prompt_text}]
        response = ""
        for chunk in self.model_client.chat(messages):
            response += chunk
        
        return {
            "prompt": prompt_text,
            "response": response
        } 