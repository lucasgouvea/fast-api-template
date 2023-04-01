from typing import Union

import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("fast_api_template.__init__:app", host="0.0.0.0", port=8000, reload=True)