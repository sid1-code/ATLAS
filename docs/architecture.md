# ATLAS V1 Architecture

V1 is a modular monolith. The browser talks to the versioned FastAPI API, routes delegate to application services, and services use SQLAlchemy persistence. The `AIService` class is a provider-neutral seam for the next milestone; it currently returns a clearly marked development response rather than pretending to call a model.

The frontend never receives database credentials and never talks directly to PostgreSQL. API schemas are separate from SQLAlchemy models. Future tools should be exposed through backend-controlled services and should follow `READ -> ANALYZE -> SUGGEST -> CONFIRM -> EXECUTE` for sensitive actions.

PostgreSQL is the only runtime datastore. Docker Compose supplies it with a named persistent volume. Alembic is intentionally deferred until migrations are needed beyond the initial schema bootstrap.


