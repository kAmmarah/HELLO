# Project: Agentic AI - Gemini Free API
# Author: Ammara Dawood

from fastapi import FastAPI, Request
from pydantic import BaseModel
from gemini_agent import ask_gemini
import uvicorn

app = FastAPI(title="Agentic AI - Gemini Free API by Ammara Dawood")

class PromptInput(BaseModel):
    prompt: str

@app.get("/")
async def home():
    return {"message": "Welcome to Gemini Agentic AI by Ammara Dawood!"}

@app.post("/ask")
async def ask_agent(input_data: PromptInput):
    response = ask_gemini(input_data.prompt)
    return {"response": response}

@app.get("/docs")
async def get_docs():
    return {"message": "Visit the documentation at /docs for more information."}

@app.get("/openapi.json")
async def get_openapi():
    return {"message": "Visit the documentation at /docs for more information."}

@app.get("/favicon.ico")
async def get_favicon():
    return {"message": "No favicon found."}

@app.get("/robots.txt")
async def get_robots():
    return {"message": "User-agent: *\nDisallow: /"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)