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


@app.post("/post-audio/")
async def post_audio(file:UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    #Декод жасайауға фунция
    message_decoded = convert_audio_to_text(audio_input)

    # если сообщения не докодировано вернем ошибку
    if not message_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode audio")


    chat_response=get_chat_response(message_decoded)

    store_messages(message_decoded, chat_response)

    if not chat_response:
        raise HTTPException(status_code=400, detail="Failed chat response")

    audio_output=convert_text_to_speech(chat_response)


    if not audio_output:
        raise HTTPException(status_code=400, detail="Failed audio output")
    def iterfile():
        yield audio_output

    return StreamingResponse(iterfile(), media_type="application/octet-stream")