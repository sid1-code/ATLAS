# Database and API

## Tables

- `users`: local user identity and timestamps.
- `conversations`: user-owned conversation metadata.
- `messages`: ordered user and assistant content.

## Endpoints

- `GET /health` returns `{ "status": "ok" }`.
- `POST /api/v1/conversations` accepts `{ "user_id": 1, "title": "..." }`.
- `GET /api/v1/conversations/{conversation_id}` returns conversation metadata and messages.
- `POST /api/v1/chat` accepts `{ "conversation_id": 1, "user_id": 1, "message": "..." }`. It creates a conversation when the ID is omitted, persists both messages, and returns the assistant response.


