# LTX-Video Quick Start

A simple guide to generate videos using LTX-Video with custom model paths.

## Setup

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

## Generate a Video

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
   - Verify the model path in `inference.py`
   - Check if the model file exists in `../../ai_models/ltxv/`

2. **CUDA errors**
   - Ensure you have enough GPU memory
   - Try reducing resolution or number of frames

For more detailed documentation, see [2.README.md](2.README.md). 