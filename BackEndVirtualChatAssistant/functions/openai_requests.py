import openai
from decouple import config


openai.organization= config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")


def convert_audio_to_text(audio_file):
  try:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    message_text = transcript["text"]
    return message_text
  except Exception as e:
    print(e)
    return



