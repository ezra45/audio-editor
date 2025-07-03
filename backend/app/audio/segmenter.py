from config import segmenter

def get_speech_segments(file_path):
    segments = segmenter(file_path)
    return [s for s in segments if s[0] == "speech"]