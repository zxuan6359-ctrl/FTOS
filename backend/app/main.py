from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="FTOS API",
    description="Foreign Trade Operating System AI Platform",
    version="2.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "name": "FTOS",
        "version": "2.0",
        "status": "running"
    }


@app.get("/api/dashboard")
def dashboard():

    return {
        "products": 0,
        "customers": 0,
        "platforms": 0,
        "ai_tasks": 0
    }


@app.get("/api/ai/status")
def ai_status():

    return {
        "openai": True,
        "langchain": True,
        "agent": "ready"
    }