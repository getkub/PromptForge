# Web Interface Guide

The Local LLM Interface includes a web-based graphical user interface (GUI) that makes it easy to browse, select, and run examples without using the command line.

## Starting the Web Interface

To launch the web interface, run:

```bash
./run_web.sh
```

This script:
1. Activates the Python virtual environment
2. Installs any required dependencies
3. Starts a FastAPI server at http://localhost:8000

Once running, open your web browser and navigate to http://localhost:8000 to access the interface.

## Features

### Home Page

![Web GUI Home](../images/web-gui-home.png)

The home page provides:
- An overview of the interface
- Quick links to example categories
- System status (whether Ollama is running)

### Example Browser

![Example Browser](../images/web-gui-examples.png)

The example browser allows you to:
- Browse available examples by domain (medical, creative, business, etc.)
- See descriptions for each example
- Select an example to run

### Running Examples

![Running Examples](../images/web-gui-run.png)

After selecting an example:
1. The system loads the corresponding template and parameters
2. You can view the formatted prompt before sending to the model
3. Click "Generate Response" to run the example
4. The interface displays the response in real-time with a progress indicator

### Response Viewing

![Response View](../images/web-gui-response.png)

The response viewer:
- Formats the output in a readable way
- Provides syntax highlighting for code blocks
- Allows copying the response to clipboard
- Lets you save the response to a file

## Advanced Features

### Parameter Customization

![Parameter Customization](../images/web-gui-parameters.png)

For any example, you can:
- View the default parameters
- Modify parameters before running
- Reset to default values

### Model Selection

The interface allows you to select from available models:
1. Click the "Model" dropdown in the top right
2. Select from available models pulled by Ollama
3. The selected model will be used for all subsequent requests

## Using with Custom Templates

You can use the web interface with your own custom templates:
1. Add your template files to the appropriate directory in `config/prompts/`
2. Create example files in the corresponding examples directory
3. Refresh the web interface to see your new examples

## Troubleshooting the Web Interface

If you encounter issues:

1. **Server won't start**
   - Check if another process is using port 8000
   - Ensure all dependencies are installed
   - Look for error messages in the terminal

2. **Examples not loading**
   - Verify your example YAML files have the correct format
   - Check console logs in your browser's developer tools
   - Ensure the file paths follow the expected structure

3. **Responses not generating**
   - Verify Ollama is running and accessible
   - Check that the selected model is available locally
   - Look for network errors in the browser's developer tools

For more detailed troubleshooting, refer to the [Troubleshooting Guide](troubleshooting.md). 