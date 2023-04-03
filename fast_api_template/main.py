from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .modules.user import routes as user_routes

app = FastAPI()

Instrumentator().instrument(app).expose(app)
app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}