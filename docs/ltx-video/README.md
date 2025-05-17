# LTX-Video Quick Start

A simple guide to generate videos using LTX-Video with custom model paths.

## Option 1: Direct Python Script

### Setup

1. Clone the LTX-Video repository:
   ```bash
   git clone https://github.com/Lightricks/LTX-Video ../Lightricks/LTX-Video
   ```

2. Download the model:
   - Manually download `ltxv-13b-0.9.7-distilled.safetensors`
   - Place it in `../../ai_models/ltxv/`

3. Modify the inference script:
   ```python
   # In inference.py, update the model path:
   pipe = LTXConditionPipeline.from_pretrained(
       "../../ai_models/ltxv/ltxv-13b-0.9.7-distilled",
       torch_dtype=torch.bfloat16
   )
   ```

### Generate a Video

Run the inference script with your prompt:

```bash
python inference.py \
    --prompt "A serene lake at sunrise" \
    --height 512 \
    --width 768 \
    --num_frames 121 \
    --seed 42 \
    --pipeline_config configs/ltxv-13b-0.9.7-distilled.yaml
```

## Option 2: Using ComfyUI (Recommended)

ComfyUI provides a user-friendly interface and better workflow management.

### Setup

1. Install ComfyUI:
   ```bash
   git clone https://github.com/comfyanonymous/ComfyUI
   cd ComfyUI
   pip install -r requirements.txt
   ```

2. Create custom model directories:
   ```bash
   # Create directories for models
   mkdir -p ../../ai_models/ComfyUI/models/checkpoints
   mkdir -p ../../ai_models/ComfyUI/models/clip
   ```

3. Download and place the models:
   - Place `ltx-video-2b-v0.9.1.safetensors` in:
     ```
     ../../ai_models/ComfyUI/models/checkpoints/ltx-video-2b-v0.9.1.safetensors
     ```
   - Place `t5xxl_fp16.safetensors` in:
     ```
     ../../ai_models/ComfyUI/models/clip/t5xxl_fp16.safetensors
     ```

4. Configure ComfyUI to use custom paths:
   ```bash
   # Create a custom config file
   cat > extra_model_paths.yaml << EOL
   checkpoints: ../../ai_models/ComfyUI/models/checkpoints
   clip: ../../ai_models/ComfyUI/models/clip
   EOL
   ```

5. Start ComfyUI with custom config:
   ```bash
   python main.py --extra-model-paths-config extra_model_paths.yaml
   ```

6. Open your browser and go to `http://localhost:8188`

### Using ComfyUI

1. Load the LTX-Video workflow:
   - Click "Load" in ComfyUI
   - Select the LTX-Video workflow file

2. Configure your generation:
   - Set your text prompt
   - Adjust video parameters (resolution, frames, etc.)
   - Click "Queue Prompt" to start generation

### Advantages of ComfyUI

- Visual workflow editor
- Real-time preview
- Better resource management
- Easier parameter adjustment
- Built-in model management
- Progress visualization

## Parameters

- `--prompt`: Text description of the video
- `--height`: Video height (default: 512)
- `--width`: Video width (default: 768)
- `--num_frames`: Number of frames to generate (default: 121)
- `--seed`: Random seed for reproducibility
- `--pipeline_config`: Path to the pipeline configuration file

## Example Prompts

Try these example prompts:
- "A serene lake at sunrise"
- "A futuristic cityscape at night"
- "Ocean waves crashing on rocks"
- "A forest path in autumn"

## Troubleshooting

If you encounter issues:

1. **Model not found**
   - Verify the model paths in your chosen method
   - Check if the model files exist in the correct directories
   - Ensure the `extra_model_paths.yaml` file is properly configured

2. **CUDA errors**
   - Ensure you have enough GPU memory
   - Try reducing resolution or number of frames
   - In ComfyUI, adjust the VRAM optimization settings

3. **ComfyUI specific**
   - Check if all required nodes are installed
   - Verify model compatibility with your ComfyUI version
   - Clear the cache if you encounter memory issues
   - Verify the custom paths are correctly set in `extra_model_paths.yaml`

For more detailed documentation, see [2.README.md](2.README.md). 