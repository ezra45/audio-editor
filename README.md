for planning, to be updated

# Audio Editor Web App

## Overview
A web application for uploading, analyzing, and interactively editing long audio files (e.g., radio shows). Users can upload audio, specify content to cut (e.g., "any talk of weather"), review AI-suggested regions, interactively edit the waveform, and download the final result. No login or persistent storage required.

---

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entrypoint, API routing
│   │   ├── config.py            # Configuration and setup
│   │   ├── jobs.py              # Job management (background tasks, progress)
│   │   ├── file_manager.py      # Temp file handling, cleanup
│   │   ├── nlp.py               # AI/NLP for semantic region detection
│   │   ├── audio/
│   │   │   ├── uploader.py      # File upload logic
│   │   │   ├── segmenter.py     # Speech/music segmentation
│   │   │   ├── chunker.py       # Audio chunking
│   │   │   ├── transcriber.py   # Transcription and language detection
│   │   │   └── __init__.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── uploads/                 # Temp storage (should be /tmp in prod)
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   ├── api.js               # API calls to backend
│   │   ├── wavesurfer.js        # Waveform display and region editing
│   │   └── ...
│   ├── package.json
│   └── ...
├── README.md
└── ...
```

---

## Backend Responsibilities
- **/upload**: Accept audio file, validate, store temp, return file ID.
- **/process**: Accept file ID and user parameters, start background job, return job ID.
- **/progress/{job_id}**: Return job progress/status.
- **/regions/{job_id}**: Return suggested regions for editing.
- **/delete/{file_id}**: Delete temp files (or auto-cleanup after timeout).
- **Validation**: File type, size, rate limiting.
- **AI/NLP**: Semantic matching of user parameters to transcript regions.
- **Language detection**: Auto-detect language before transcription.

## Frontend Responsibilities
- File upload UI
- Parameter input and management
- Waveform display and region editing (wavesurfer.js)
- Progress bar (polls backend)
- Download edited file
- All edit history/undo/redo logic

---

## Key Architectural Decisions
- **Stateless, session-based**: No persistent user data; temp files and jobs are referenced by tokens/IDs.
- **Async/background jobs**: User gets progress updates while processing.
- **No authentication**: For single-user or small-team use.
- **No database**: All state is ephemeral.
- **Rate limiting**: Prevent abuse (e.g., 10 files/day per IP).

---

## Development & Testing
- **Backend**: Python, FastAPI, Docker, pytest, slowapi (rate limiting), Celery/Redis (for robust background jobs)
- **Frontend**: React, wavesurfer.js
- **CI/CD**: GitHub Actions for linting, testing, and deployment

---

## Next Steps
1. Refactor backend to match this structure
2. Implement function skeletons for new modules
3. Add file validation, rate limiting, and background job support
4. Integrate advanced NLP for semantic region detection
5. Build frontend with waveform editing and API integration 