# Travel with Farmer 🌱

**Travel with Farmer** is an AI-powered agriculture and agri-tourism platform built for farmers. It combines sustainable farming guidance, disease diagnosis, NDVI crop monitoring, weather intelligence, market prices, and a social learning community.

## Platform Highlights

- **Bhoomi AI Assistant** (LLM-powered, multilingual-ready) for crop planning and pest guidance.
- **Plant Disease Detection** via CNN-style image classifier service.
- **Weather Advisory** with irrigation recommendations.
- **Market Price Intelligence** with nearby mandi comparisons.
- **Agri Tourism** farm discovery and booking-ready data model.
- **Satellite Monitoring** NDVI endpoints for crop stress.
- **Community Hub** for short video sharing and farmer discussions.

## Monorepo Structure

```text
.
├── backend/                 # FastAPI + PostgreSQL + AI services
├── frontend/                # Flutter app (Android/iOS/Web)
├── deploy/                  # Docker and deployment assets
└── docs/                    # Architecture and database docs
```

## Quick Start

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Backend docs: http://localhost:8000/docs

### 2) Frontend (Flutter)

```bash
cd frontend
flutter pub get
flutter run -d chrome
```

> Update `lib/core/config.dart` to point to your backend host.

### 3) Full stack with Docker

```bash
docker compose -f deploy/docker-compose.yml up --build
```

## Required API Endpoints

Implemented in FastAPI:

- `GET /`
- `POST /bhoomi-chat`
- `POST /plant-diagnosis`
- `GET /weather`
- `GET /market-prices`
- `GET /nearby-farms`
- `POST /upload-video`

## Production Notes

- Uses async SQLAlchemy and PostgreSQL.
- AI providers are abstracted in service classes with safe fallbacks.
- Env-based secrets and API keys.
- Docker-ready with isolated backend/frontend services.

See `docs/architecture.md` and `docs/database.md` for deeper implementation details.
