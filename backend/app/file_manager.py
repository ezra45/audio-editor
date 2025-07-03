# file_manager.py
from typing import Optional

def save_temp_file(upload_file) -> str:
    """Save an uploaded file to a temp directory and return a file ID."""
    pass

def get_temp_file_path(file_id: str) -> Optional[str]:
    """Get the file path for a given file ID."""
    pass

def delete_temp_file(file_id: str):
    """Delete a temp file by its file ID."""
    pass

def cleanup_expired_files():
    """Periodically clean up expired temp files."""
    pass 