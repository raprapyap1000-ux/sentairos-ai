from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
import subprocess
import json
from gtts import gTTS # Lightweight fallback, will explain local ONNX/Piper
import pygame # To play sounds locally
from dotenv import load_dotenv

load_dotenv()
pygame.mixer.init()

app = FastAPI(title="Sentairos AI Backend")
# ... (rest of the previous code remains)

# Allow local frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CONFIG_FILE = "sentairos_config.json"

def get_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"api_key": ""}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

class ChatRequest(BaseModel):
    message: str
    provider: str = "gemini"

class ConfigUpdate(BaseModel):
    api_key: str

class ExecRequest(BaseModel):
    command: str

@app.post("/set_api_key")
async def set_api_key(request: ConfigUpdate):
    save_config({"api_key": request.api_key})
    return {"status": "API Key saved locally."}

@app.post("/chat")
async def chat(request: ChatRequest):
    config = get_config()
    api_key = config.get("api_key")
    
    if not api_key:
        raise HTTPException(status_code=400, detail="API Key is missing. Please set it in settings.")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    try:
        response = model.generate_content(request.message)
        return {"reply": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/terminal")
async def execute_command(request: ExecRequest):
    try:
        # Full terminal access as requested
        result = subprocess.run(request.command, shell=True, capture_output=True, text=True, timeout=30)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        return {"stdout": "", "stderr": str(e), "returncode": 1}

@app.post("/voice")
async def play_voice(request: ChatRequest):
    try:
        # For anime feel, we recommend Piper (Local) or Bark.
        # Here is a lightweight local-execution flow:
        tts = gTTS(text=request.message, lang='en')
        temp_file = "speech.mp3"
        tts.save(temp_file)
        
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        
        return {"status": "playing"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
