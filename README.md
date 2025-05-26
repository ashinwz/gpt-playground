# gpt-playground

A simple chatbot application built with Vue 3 + Vite on the frontend and FastAPI on the backend. Everything runs with Docker Compose and uses Google's Gemini API for responses.

## Requirements
- Docker
- Docker Compose

## Usage

1. Copy `.env` and adjust values if needed. Set `GEMINI_API_KEY` to your Google Gemini API key.
2. Build and start the stack:

```bash
docker-compose up --build
```

The frontend will be available at <http://localhost:5173> and will proxy requests to the FastAPI backend running on port 8000.

## Project structure

- `backend/` – FastAPI application
- `frontend/` – Vite + Vue 3 application
- `docker-compose.yml` – starts both services

The backend forwards messages to Google's Gemini API. Adjust `backend/main.py` if you wish to use a different service.
