from llm_interface.model_client import ModelClient
from llm_interface.prompt_manager import PromptManager
import os
import datetime
import json
import yaml
import argparse

def save_response(content: str, prompt_text: str, output_dir: str = "output") -> None:
    """Save the response and prompt to files with timestamps."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save the response
    output_file = os.path.join(output_dir, f"response_{timestamp}.txt")
    with open(output_file, "w") as f:
        f.write(content)
    print(f"\nResponse saved to: {output_file}")
    
    # Save the prompt
    prompt_file = os.path.join(output_dir, f"prompt_{timestamp}.txt")
    with open(prompt_file, "w") as f:
        f.write(prompt_text)
    print(f"Prompt saved to: {prompt_file}")

def load_example(example_path: str) -> dict:
    """Load an example from a YAML file."""
    with open(example_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description='Run LLM examples')
    parser.add_argument('example_path', help='Path to the example YAML file')
    args = parser.parse_args()

    # Load the example
    try:
        example = load_example(args.example_path)
    except Exception as e:
        print(f"Error loading example file: {e}")
        return

    # Initialize the model client and prompt manager
    client = ModelClient()
    prompt_manager = PromptManager()

    # List available prompts
    print("\nAvailable prompts:")
    for prompt in prompt_manager.list_prompts():
        print(f"- {prompt['id']}: {prompt['name']}")
        print(f"  Description: {prompt['description']}")
        print(f"  Domain: {prompt['domain']}.{prompt['subdomain']}")
        print()

    # Format the prompt with the example parameters
    prompt_text = prompt_manager.format_prompt(example['prompt_id'], **example['parameters'])
    
    if prompt_text:
        # Create the message
        messages = [{"role": "user", "content": prompt_text}]
        
        # Get the response and save to file
        print(f"\nRunning example: {example['name']}")
        print(f"Description: {example['description']}")
        print("\nGenerating response...")
        full_response = ""
        
        try:
            for chunk in client.chat(messages, stream=True):
                print(chunk, end="", flush=True)
                full_response += chunk
            
            # Save the response and prompt
            save_response(full_response, prompt_text)
            
        except Exception as e:
            print(f"\nError generating response: {e}")
    else:
        print("Failed to format prompt. Check the parameters and try again.")

if __name__ == "__main__":
    main() 