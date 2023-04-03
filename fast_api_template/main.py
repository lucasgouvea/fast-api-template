import uvicorn

from fastapi import FastAPI
from .modules.user import routes as user_routes

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("fast_api_template.main:app", host="0.0.0.0", port=8000, reload=True)