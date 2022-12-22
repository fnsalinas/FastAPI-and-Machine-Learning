
from pathlib import Path

import torch
from diffusers import StableDiffusionPipeline
from PIL.Image import Image

token_path = Path("token.txt")
token = token_path.read_text().strip()

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    revision = "fp16",
    torch_dtype = torch.float16,
    use_auth_token = token
    )

pipe.to("cuda")

prompt = "a photograph of an astronaut riding a horse"

image = pipe(prompt)["sample"][0]

def obtaiun_image(
    prompt: str,
    *,
    seed: int = None,
    num_inferecnce_steps: int = 50,
    guidance_scale: float = 7.5
) -> Image:
    generator = None if seed is None else torch.Generator("cuda").manual_seed(1024)
    print(f"Using devuce: {pipe.device}")
    image: Image = pipe(
        prompt,
        guidance_scale = guidance_scale,
        num_inferecnce_steps = num_inferecnce_steps,
        generator = generator
    ).images[0]
    return image