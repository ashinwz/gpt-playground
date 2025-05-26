# gpt-playground

A simple ChatGPT-like application built with Vue 3 + Vite on the frontend and FastAPI on the backend. Everything runs with Docker Compose.

## Requirements
- Docker
- Docker Compose

## Usage

1. Copy `.env` and adjust values if needed.
2. Build and start the stack:

```bash
docker-compose up --build
```

The frontend will be available at <http://localhost:5173> and will proxy requests to the FastAPI backend running on port 8000.

### Local Python environment

If you prefer to run the backend without Docker, create a virtual environment:

```bash
./scripts/setup_venv.sh
source venv/bin/activate
uvicorn backend.main:app --reload
```

## Project structure

- `backend/` – FastAPI application
- `frontend/` – Vite + Vue 3 application
- `docker-compose.yml` – starts both services

This setup uses a simple echo response in the backend. Integrate your own model or API by editing `backend/main.py`.
