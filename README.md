# ATLAS V1

ATLAS is a local-first personal AI operating system. This repository contains the Milestone 1 foundation: a Next.js frontend, a FastAPI backend, PostgreSQL persistence, and a replaceable AI service boundary.

## Requirements

- Node.js 20+
- Python 3.11+
- Docker with Docker Compose v2

## Run locally

1. Copy `.env.example` to `.env`.
2. Start PostgreSQL:

   ```powershell
   docker compose up -d postgres
   ```

3. In one terminal, install and run the backend:

   ```powershell
   cd backend
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```

4. In another terminal, install and run the frontend:

   ```powershell
   cd frontend
   npm install
   npm run dev
   ```

Open http://localhost:3000. The backend health endpoint is http://localhost:8000/health.

## Test

```powershell
cd backend
pytest

cd ..\frontend
npm run lint
npm run build
```

The initial chat response is intentionally a development placeholder until an AI provider is selected. See [docs/architecture.md](docs/architecture.md) and [docs/database-api.md](docs/database-api.md) for boundaries and API contracts.
