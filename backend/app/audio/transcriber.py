from config import model

def transcribe_chunks(chunk_paths, orig_starts):
    """
    Transcribe each chunk and return a list of dicts with absolute start, end, and text.
    The start/end are relative to the original audio.
    chunk_paths: list of chunk file paths
    orig_starts: list of original start times for each chunk
    """
    segments = []
    for path, orig_start in zip(chunk_paths, orig_starts):
        result = model.transcribe(path, fp16=False, word_timestamps=False)
        for seg in result["segments"]:
            segments.append({
                "original_start": orig_start + seg["start"],
                "original_end": orig_start + seg["end"],
                "text": seg["text"].strip()
            })
    return segments