from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from audio.uploader import save_file
from audio.segmenter import get_speech_segments
from audio.chunker import extract_speech_chunks
from audio.transcriber import transcribe_chunks
from audio.mapping import merge_segments_to_sentences
from config import UPLOAD_DIR
#import jobs, file_manager, nlp

app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    """Upload an audio file, validate, and store it temporarily. Returns mapped speech segments with original timestamps."""
    try:
        file_path = save_file(file, UPLOAD_DIR)
        speech_segments = get_speech_segments(file_path)
        chunk_paths = extract_speech_chunks(file_path, speech_segments)
        orig_starts = [seg[1] for seg in speech_segments]  # original start times for each chunk
        whisper_segments = transcribe_chunks(chunk_paths, orig_starts)
        merged = merge_segments_to_sentences(whisper_segments)
        return {"filename": file.filename, "segments": merged}
    except Exception as e:
        return {"error": str(e)}

@app.post("/process")
async def process_audio(file_id: str, parameters: list, background_tasks: BackgroundTasks = None):
    """Start background processing of the audio file with user parameters. Returns a job ID."""
    pass

@app.get("/progress/{job_id}")
def get_progress(job_id: str):
    """Get the progress/status of a processing job."""
    pass

@app.get("/regions/{job_id}")
def get_regions(job_id: str):
    """Get the suggested regions for editing from a completed job."""
    pass

@app.delete("/delete/{file_id}")
def delete_file(file_id: str):
    """Delete a temporary file and associated job data."""
    pass