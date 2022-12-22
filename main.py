from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id,
        "message": "Hello World"
        }

class Item(BaseModel):
    name: str
    price: float
    tags: List[str] = []

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/generate")
def generate_image(prompt: str):
    return {"prompt": prompt}

