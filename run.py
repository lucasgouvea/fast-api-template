import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

stage = os.getenv("APP_STAGE")
port = int(os.getenv("APP_PORT"))

if __name__ == "__main__" and stage != "PROD":
    uvicorn.run("fast_api_template.main:app", host="0.0.0.0", port=port, reload=True)

if __name__ == "__main__" and stage == "PROD":
    uvicorn.run("fast_api_template.main:app", host="0.0.0.0", port=port)