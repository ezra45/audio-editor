from dotenv import load_dotenv
load_dotenv()

import whisper
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI()

# middleware
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

model = whisper.load_model("base")

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    print("yas")
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    print("yas1")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("yas2")
    result = model.transcribe(file_path)
    print("yas3")
    return {
        "filename": file.filename,  
        "transcription":result["text"]
        }