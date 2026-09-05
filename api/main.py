from fastapi import FastAPI
from pydantic import BaseModel

from src.graph.workflow import graph


app = FastAPI(title="AI Research Agent API")


class ResearchRequest(BaseModel):
    topic: str


@app.get("/")
def home():
    return {
        "message": "AI Research Agent API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/research")
def research(request: ResearchRequest):
    result = graph.invoke({
        "topic": request.topic
    })

    return result