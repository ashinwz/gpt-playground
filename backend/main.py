from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str


async def generate_with_gemini(message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-pro:generateContent?key={api_key}"
    )
    payload = {"contents": [{"parts": [{"text": message}]}]}
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(url, json=payload)
        try:
            resp.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        data = resp.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        raise HTTPException(status_code=500, detail="Invalid response from Gemini API")

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    response_text = await generate_with_gemini(req.message)
    return ChatResponse(response=response_text)

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("FASTAPI_HOST", "0.0.0.0")
    port = int(os.getenv("FASTAPI_PORT", 8000))
    uvicorn.run("main:app", host=host, port=port)
