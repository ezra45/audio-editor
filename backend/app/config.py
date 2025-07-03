import os
import whisper
from inaSpeechSegmenter import Segmenter

UPLOAD_DIR = "../uploads"
CHUNK_DIR = "../uploads/chunks"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CHUNK_DIR, exist_ok=True)

model = whisper.load_model("base")
segmenter = Segmenter(vad_engine='sm', detect_gender=False)