from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


app = FastAPI()

@app.get("/chat")
async def chat_asisstant():
    return {"response":"chat"}


@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"response": "conversation reset"}