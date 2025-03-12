from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

from functions.openai_requests import convert_audio_to_text
app = FastAPI()

@app.get("/chat")
async def chat_asisstant():
    return {"response":"chat"}


# @app.get("/reset")
# async def reset_conversation():
#     reset_messages()
#     return {"response": "conversation reset"}


@app.post("/post-audio/")
async def get_audio():
    audio_input = open("voice.mp3","rb")
    message_decoded = convert_audio_to_text(audio_input)
    print(message_decoded)
    return "Done"

