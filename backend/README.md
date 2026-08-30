# COLLEXA Backend - Intelligent Chat Agent for KEC

Professional FastAPI backend for COLLEXA, the intelligent chat agent for Kathmandu Engineering College.

## Project Structure

```
backend/
├── main.py                 # FastAPI app entry point
├── config.py              # Configuration management
├── database.py            # Database connection
├── models.py              # SQLAlchemy ORM models
├── schemas.py             # Pydantic request/response schemas
├── auth.py                # Authentication & JWT
├── rag_system.py          # RAG system with ChromaDB
├── routers/               # API route handlers
│   ├── auth.py           # Authentication endpoints
│   ├── chat.py           # Chat/COLLEXA endpoints
│   ├── appointments.py    # Appointment booking
│   ├── seats.py          # Seat availability & reservations
│   ├── registrations.py  # Program registrations
│   └── results.py        # Student results
└── pyproject.toml        # Dependencies

```

## Setup

### 1. Install Dependencies

```bash
pip install -e .
```

### 2. Environment Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Update these critical values:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT signing key (generate with `openssl rand -hex 32`)
- `GOOGLE_API_KEY`: Google Gemini API key

### 3. Database Setup

```bash
alembic upgrade head
```

### 4. Run Development Server

```bash
python main.py
```

Server will start at `http://localhost:8000`

## API Documentation

- **Interactive Docs**: `http://localhost:8000/api/docs`
- **ReDoc**: `http://localhost:8000/api/redoc`

## Key Features

- **Authentication**: JWT-based user authentication
- **RAG System**: ChromaDB for knowledge base retrieval
- **COLLEXA Agent**: LLM-powered chat agent (LangGraph)
- **Appointments**: Faculty appointment booking system
- **Seat Management**: Program seat availability & reservations
- **Registrations**: Student registration tracking
- **Results**: Academic result management

## Authentication

All protected endpoints require a Bearer token:

```
Authorization: Bearer <access_token>
```

Get a token via `/api/auth/login` or `/api/auth/register`.

## Development

### Code Quality

```bash
# Format code
black .

# Lint
ruff check .

# Type checking
mypy .
```

### Testing

```bash
pytest
```

## Deployment

Docker ready. See `Dockerfile` for production deployment.
