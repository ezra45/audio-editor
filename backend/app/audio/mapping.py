import typing as t
import re

def safe_round(value, ndigits=2):
    return round(value, ndigits) if value is not None else None

def merge_segments_to_sentences(segments: t.List[dict]) -> t.List[dict]:
    merged = []
    buffer = ""
    start_time = None
    end_time = None

    for seg in segments:
        if start_time is None:
            start_time = seg["original_start"]
        buffer += (" " if buffer else "") + seg["text"]
        end_time = seg["original_end"]

        if re.search(r"[.!?][\"')\]]*\s*$", buffer):
            merged.append({
                "original_start": safe_round(start_time, 2),
                "original_end": safe_round(end_time, 2),
                "text": buffer.strip()
            })
            buffer = ""
            start_time = None
            end_time = None

    if buffer:
        merged.append({
            "original_start": safe_round(start_time, 2),
            "original_end": safe_round(end_time, 2),
            "text": buffer.strip()
        })

    return merged