from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Message
from chatbot import process_chat
import json

app = FastAPI(
    title="API Chatbot Vêtements",
    description="Assistant de commande de vêtements en ligne",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "API Chatbot Vêtements opérationnelle"}

@app.post("/chat/")
async def chat_endpoint(messages: List[Message]):
    try:
        result = process_chat([m.dict() for m in messages])

        if result["type"] == "order":
            try:
                order = json.loads(result["content"])
                return {"response": "Commande prête!", "order": order}
            except Exception as e:
                return {
                    "response": result["content"],
                    "order": None,
                    "error": f"Erreur JSON: {str(e)}"
                }

        return {"response": result["content"], "order": None}
    
    except Exception as e:
        return {"error": f"Erreur lors du traitement: {str(e)}"}
