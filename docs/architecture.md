# System Architecture

## High-level Flow

`Flutter App -> FastAPI Backend -> AI/External Services -> PostgreSQL`

### Backend modules

- `api/routes.py`: HTTP surface.
- `services/`: domain and AI orchestration.
- `models/`: SQLAlchemy ORM entities.
- `schemas/`: Pydantic request/response contracts.

### AI services

1. **Bhoomi LLM Service**: handles multilingual advisory chat.
2. **Disease Detection Service**: CNN-compatible inference facade.
3. **Speech-to-text**: client-side Flutter plugin (`speech_to_text`) for voice input.
4. **NDVI Processing**: backend placeholder service ready for Sentinel/Earth Search integration.

### Integrations

- OpenWeatherMap for weather and irrigation logic.
- Market price provider for mandi and trend data.
- Satellite provider (STAC compatible) for NDVI data.
