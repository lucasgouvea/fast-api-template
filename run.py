import uvicorn

if __name__ == "__main__":
    uvicorn.run("fast_api_template.main:app", host="0.0.0.0", port=3000, reload=True)
