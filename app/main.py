# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    # Perform health checks here (e.g., database connectivity)
    return {"status": "healthy"}

@app.get("/")
def read_root():
    return {"Hello": "World"}
