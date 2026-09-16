from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI application
app = FastAPI(
    title="Sayeed Ahmad - Claude LLM API",
    description="FastAPI application for interacting with Anthropic Claude",
    version="1.0.0"
)

# Get Anthropic API key
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set in the .env file")

# Create Anthropic client
client = Anthropic(api_key=api_key)


# -----------------------------
# Request / Response Models
# -----------------------------

class ChatRequest(BaseModel):
    message: str
    max_tokens: int = 200


class ChatResponse(BaseModel):
    response: str
    model: str
    input_tokens: int
    output_tokens: int


# -----------------------------
# Home Endpoint
# -----------------------------

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Welcome to Sayeed Ahmad's Claude API"
    }


# -----------------------------
# Chatbot Endpoint
# -----------------------------

@app.post("/chatbot")
def chatbot(req: ChatRequest):

    if not req.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    def generate():

        try:
            with client.messages.stream(
                model="claude-haiku-4-5-20251001",
                max_tokens=req.max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": req.message
                    }
                ],
            ) as stream:

                for text in stream.text_stream:
                    yield f"data: {text}\n\n"

                yield "data: [DONE]\n\n"

        except Exception as e:
            yield f"data: Error: {str(e)}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )