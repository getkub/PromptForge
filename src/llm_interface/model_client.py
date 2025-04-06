import requests
import json
from typing import List, Dict, Optional, Generator
import sys

class ModelClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip('/')
        self.chat_endpoint = f"{self.base_url}/api/chat"
        print(f"Initialized ModelClient with endpoint: {self.chat_endpoint}")

    def chat(
        self,
        messages: List[Dict[str, str]],
        model: str = "gemma3:27b",
        stream: bool = True,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Send a chat request to the model and yield responses.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model identifier
            stream: Whether to stream the response
            **kwargs: Additional parameters to pass to the API
        
        Yields:
            Response chunks if streaming, or complete response if not streaming
        """
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream,
            **kwargs
        }

        print(f"Sending request to {self.chat_endpoint}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        try:
            response = requests.post(
                self.chat_endpoint,
                json=payload,
                stream=stream,
                timeout=60  # Add a timeout
            )
            response.raise_for_status()
            
            if stream:
                print("Processing streaming response...")
                for line in response.iter_lines():
                    if line:
                        try:
                            chunk = json.loads(line)
                            # Check for the message content in the response
                            if 'message' in chunk and 'content' in chunk['message']:
                                yield chunk['message']['content']
                            elif 'response' in chunk:
                                yield chunk['response']
                            elif 'error' in chunk:
                                print(f"Error from model: {chunk['error']}", file=sys.stderr)
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON: {e}", file=sys.stderr)
                            print(f"Raw line: {line}", file=sys.stderr)
            else:
                print("Processing non-streaming response...")
                data = response.json()
                if 'message' in data and 'content' in data['message']:
                    yield data['message']['content']
                elif 'response' in data:
                    yield data['response']
                elif 'error' in data:
                    print(f"Error from model: {data['error']}", file=sys.stderr)
        except requests.exceptions.ConnectionError:
            print(f"Connection error: Could not connect to {self.chat_endpoint}", file=sys.stderr)
            print("Make sure the model server is running.", file=sys.stderr)
            yield ""
        except requests.exceptions.Timeout:
            print("Request timed out. The model might be taking too long to respond.", file=sys.stderr)
            yield ""
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            yield "" 