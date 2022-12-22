# FastAPI-and-Machine-Learning

#### References:
- Stable Diffusion Model and code: https://huggingface.co/blog/stable_diffusion
- HuggingFace token generation: https://huggingface.co/settings/tokens
- Fix to error: https://huggingface.co/CompVis/stable-diffusion-v1-4/discussions/158
    line of code: StableDiffusionPipeline.from_pretrained
    TypeError: getattr(): attribute name must be string
    Solution: install diffusers==0.8.0 not diffusers==0.4.0
- Path to the Api documentation: http://127.0.0.1:8000/docs#/
