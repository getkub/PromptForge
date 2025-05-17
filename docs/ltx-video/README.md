# LTX-Video Quick Start

A simple guide to generate videos using LTX-Video with custom model paths.

## Setup

1. Clone the LTX-Video repository:
   ```bash
   git clone https://github.com/Lightricks/LTX-Video ../../../LTX-Video
   ```

2. Install system dependencies:
   ```bash
   # For macOS using Homebrew
   brew install cmake
   brew install pkg-config
   brew install ffmpeg
   ```

3. Create and activate a virtual environment:
   ```bash
   # Create virtual environment with Python 3.12
   /opt/homebrew/opt/python@3.12/bin/python3.12 -m venv ~/ltx-venv-py312

   # Activate the virtual environment
   source ~/ltx-venv-py312/bin/activate
   ```

4. Install dependencies:
   ```bash
   # Upgrade pip
   pip install --upgrade pip

   # Install PyTorch and related packages
   pip install torch torchvision torchaudio

   # Install video processing packages
   pip install av
   pip install imageio
   pip install imageio-ffmpeg
   pip install opencv-python

   # Install ML and utility packages
   pip install diffusers
   pip install transformers
   pip install safetensors
   pip install Pillow
   pip install pyyaml
   pip install huggingface_hub
   pip install einops

   # Install LTX-Video package
   cd ../../../LTX-Video
   pip install -e .
   cd -
   ```

5. Download the model:
   - Manually download `ltxv-13b-0.9.7-distilled.safetensors`
   - Place it in `../../ai_models/ltxv/`

6. Copy and modify the inference script:
   ```bash
   # Copy the inference script to this directory
   cp ../../../LTX-Video/inference.py .

   # The script has been modified to use the correct paths:
   # - Model path: ../../ai_models/ltxv/ltxv-13b-0.9.7-distilled
   # - Config path: ../../../LTX-Video/configs/ltxv-13b-0.9.7-distilled.yaml
   ```

### Generate a Video

Make sure you're in the docs/ltx-video directory and virtual environment is activated:
```bash
# Verify you're in the correct directory
pwd  # Should show path ending with docs/ltx-video

# Activate virtual environment if not already activated
source ~/ltx-venv-py312/bin/activate

# Run the inference script
python inference.py \
    --prompt "A serene lake at sunrise" \
    --height 512 \
    --width 768 \
    --num_frames 121 \
    --seed 42 \
    --pipeline_config ../../../LTX-Video/configs/ltxv-13b-0.9.7-distilled.yaml
```

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

1. **Module not found errors**
   - Make sure you're in the virtual environment:
     ```bash
     source ~/ltx-venv-py312/bin/activate
     ```
   - Try installing missing packages:
     ```bash
     # Video processing packages
     pip install av
     pip install imageio imageio-ffmpeg
     pip install opencv-python

     # ML and utility packages
     pip install diffusers transformers safetensors Pillow pyyaml huggingface_hub einops
     ```
   - If you get version conflicts, try:
     ```bash
     pip install --no-deps diffusers transformers safetensors
     ```
   - If you get "No module named 'ltx_video'", make sure you've installed the LTX-Video package:
     ```bash
     cd ../../../LTX-Video
     pip install -e .
     cd -
     ```

2. **Build errors**
   - Make sure system dependencies are installed:
     ```bash
     brew install cmake
     brew install pkg-config
     brew install ffmpeg
     ```
   - If you get errors about missing build tools, try:
     ```bash
     xcode-select --install
     ```

3. **Model not found**
   - Verify the model path in the modified inference.py
   - Check if the model file exists in `../../ai_models/ltxv/`
   - Ensure the config file path is correct

4. **CUDA errors**
   - Ensure you have enough GPU memory
   - Try reducing resolution or number of frames
   - Verify PyTorch is installed with CUDA support

5. **Script errors**
   - Make sure you're in the docs/ltx-video directory
   - Verify the virtual environment is activated:
     ```bash
     source ~/ltx-venv-py312/bin/activate
     ```
   - Check if all dependencies are installed correctly
   - If dependencies fail to install, try:
     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt --no-cache-dir
     ```

For more detailed documentation, see [2.README.md](2.README.md). 