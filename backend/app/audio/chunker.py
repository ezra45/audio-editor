import os
from pydub import AudioSegment
from config import CHUNK_DIR

def extract_speech_chunks(file_path, segments):
    audio = AudioSegment.from_file(file_path)
    chunk_paths = []
    for i, (_, start, end) in enumerate(segments):
        chunk = audio[start * 1000:end * 1000]
        chunk_path = os.path.join(CHUNK_DIR, f"chunk_{i}.wav")
        chunk.export(chunk_path, format="wav")
        chunk_paths.append(chunk_path)
    return chunk_paths