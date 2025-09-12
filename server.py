# server.py
import os
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from openai import OpenAI
from gtts import gTTS

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Serve static frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")

    # --- OpenAI text response ---
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI sales agent."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response.choices[0].message.content.strip()

    # --- gTTS audio response ---
    audio_filename = f"reply_{uuid.uuid4().hex}.mp3"
    audio_path = os.path.join("static", "audio", audio_filename)
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    tts = gTTS(text=reply, lang="en")
    tts.save(audio_path)

    audio_url = f"/static/audio/{audio_filename}"

    return JSONResponse({"reply": reply, "audio_url": audio_url})
