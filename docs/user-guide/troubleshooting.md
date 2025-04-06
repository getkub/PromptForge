# Troubleshooting

This guide helps you solve common issues when working with the Local LLM Interface.

## Common Issues

### Template and Prompt Issues

1. **Missing Parameter in Template Error**
   
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

### Connection Issues

1. **Cannot Connect to Ollama**
   
   Error: `Failed to connect to model server`
   
   - Verify Ollama is running in another terminal: `ollama list`
   - Check it's running on the default port (11434)
   - Ensure the model specified in your example is available locally

2. **Model Not Found**
   
   Error: `model not found: <model_name>`
   
   - Ensure you've pulled the model: `ollama pull <model_name>`
   - Check available models: `ollama list`
   - Verify the model name matches exactly (including version)

### Environment and Setup Issues

1. **Package Not Found**
   
   Error: `ModuleNotFoundError: No module named '<module>'`
   
   - Make sure you've run the setup script: `./setup.sh`
   - Ensure the virtual environment is activated
   - Try reinstalling dependencies: `pip install -r requirements.txt`

2. **Permission Denied**
   
   Error: `Permission denied: '<file_path>'`
   
   - Check file permissions: `ls -la <file_path>`
   - Make scripts executable: `chmod +x *.sh`

## Debugging Tips

1. **Enable Debug Logging**
   
   Add these lines to your script:
   
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Test Templates Individually**
   
   ```python
   from llm_interface.core.prompt_manager import PromptManager
   
   manager = PromptManager()
   template_id = "domain.templates.type.name"
   print(manager.get_template(template_id))
   ```

3. **Check API Responses**
   
   If using the web interface, check browser developer tools (Network tab) for API responses.

## Getting Help

If you're still facing issues:

1. Check the [examples documentation](../examples/working-with-templates.md) for guidance on template creation
2. Review the [prompt system documentation](prompt-system.md) for details on how templates work
3. File an issue on the project repository with detailed steps to reproduce the problem 