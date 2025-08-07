from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True, "service": os.getenv("SERVICE_NAME", "unknown")}
