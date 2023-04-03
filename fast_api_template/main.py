from fastapi import FastAPI
from .modules.user import routes as user_routes

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}