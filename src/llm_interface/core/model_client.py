"""
Module for handling interactions with the language model.
"""
import json
import requests
from typing import List, Dict, Generator, Optional

class ModelClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip("/")
    
    def chat(
        self, 
        messages: List[Dict[str, str]], 
        model: str = "gemma:3b-27b",
        stream: bool = True
    ) -> Generator[str, None, None]:
        """
        Send a chat request to the model and stream the response.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Name of the model to use
            stream: Whether to stream the response
        
        Yields:
            Generated text chunks from the model
        """
        url = f"{self.base_url}/api/chat"
        
        data = {
            "model": model,
            "messages": messages,
            "stream": stream
        }
        
        try:
            with requests.post(url, json=data, stream=True) as response:
                response.raise_for_status()
                
                for line in response.iter_lines():
                    if not line:
                        continue
                    
                    try:
                        # Parse the JSON response
                        chunk = json.loads(line)
                        
                        # Extract the message content
                        if "message" in chunk and "content" in chunk["message"]:
                            yield chunk["message"]["content"]
                        
                        # Check for errors
                        if "error" in chunk:
                            raise ValueError(f"Model error: {chunk['error']}")
                            
                    except json.JSONDecodeError:
                        # If not JSON, yield the raw line
                        yield line.decode('utf-8')
                        
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to model server: {e}")
    
    def generate(
        self,
        prompt: str,
        model: str = "gemma:3b-27b",
        stream: bool = True,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Generate text from a prompt.
        
        Args:
            prompt: The input prompt
            model: Name of the model to use
            stream: Whether to stream the response
            **kwargs: Additional parameters for the model
        
        Yields:
            Generated text chunks
        """
        url = f"{self.base_url}/api/generate"
        
        data = {
            "model": model,
            "prompt": prompt,
            "stream": stream,
            **kwargs
        }
        
        try:
            with requests.post(url, json=data, stream=True) as response:
                response.raise_for_status()
                
                for line in response.iter_lines():
                    if not line:
                        continue
                    
                    try:
                        # Parse the JSON response
                        chunk = json.loads(line)
                        
                        # Extract the generated text
                        if "response" in chunk:
                            yield chunk["response"]
                        
                        # Check for errors
                        if "error" in chunk:
                            raise ValueError(f"Model error: {chunk['error']}")
                            
                    except json.JSONDecodeError:
                        # If not JSON, yield the raw line
                        yield line.decode('utf-8')
                        
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to model server: {e}") 