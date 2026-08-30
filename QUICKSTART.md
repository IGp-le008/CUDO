"""Quick start guide for COLLEXA."""

# 🚀 COLLEXA Quick Start Guide

Get the KEC website with COLLEXA chat agent running in 5 minutes!

## Prerequisites

- ✅ Docker & Docker Compose installed
- ✅ Git installed
- ✅ Google Gemini API Key (free: https://makersuite.google.com/app/apikey)

## Step-by-Step Setup

### 1. Clone & Navigate
```bash
git clone <repository-url>
cd VibeCode
```

### 2. Create Environment File
```bash
cp .env.example .env
```

Edit `.env` and add your **GOOGLE_API_KEY**:
```bash
GOOGLE_API_KEY=your-actual-api-key-here
```

### 3. Start Everything with Docker
```bash
docker-compose up -d
```

This command will:
- ✅ Create PostgreSQL database
- ✅ Start FastAPI backend (port 8000)
- ✅ Start Next.js frontend (port 3000)
- ✅ Initialize all services

### 4. Access the Application

| Service | URL | Purpose |
|---------|-----|---------|
| **Frontend** | http://localhost:3000 | Main website |
| **API Docs** | http://localhost:8000/api/docs | Interactive API docs |
| **Backend Health** | http://localhost:8000/api/health | Health check |

### 5. Create Sample Users (Optional)
```bash
# Initialize database with sample data
docker-compose exec backend python scripts/init.py
```

Sample credentials:
- **Student**: student1@kec.edu.np / TestPassword123
- **Admin**: admin@kec.edu.np / AdminPassword123

## Test the Chat Agent

1. Go to http://localhost:3000
2. Click the chat bubble in bottom-right
3. Ask COLLEXA questions like:
   - "What programs does KEC offer?"
   - "How do I apply to KEC?"
   - "What are the fees?"
   - "Who are the faculty?"

## Common Commands

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Stop Services
```bash
docker-compose down
```

### Rebuild Everything
```bash
docker-compose down
docker-compose up -d --build
```

### Access Database
```bash
docker-compose exec db psql -U collexa -d collexa_db
```

## Troubleshooting

### Port Already in Use
```bash
# Change ports in docker-compose.yml or stop other services
lsof -i :3000  # Check what's using port 3000
```

### Docker Not Running
```bash
# Start Docker daemon
# On Mac: open -a Docker
# On Linux: sudo systemctl start docker
```

### API Connection Error
```bash
# Check if backend is running
curl http://localhost:8000/api/health

# Check logs
docker-compose logs backend
```

### Frontend Won't Load
```bash
# Rebuild frontend
docker-compose build frontend
docker-compose up frontend -d
```

## Next Steps

### Development
- Edit backend: `backend/` directory
- Edit frontend: `frontend/src/` directory
- Changes auto-reload via Docker volumes

### Customization
- Update college info in `backend/knowledge_base.py`
- Customize UI in `frontend/src/components/`
- Modify colors in `frontend/tailwind.config.ts`

### Deployment
- See `DEPLOYMENT.md` for production setup
- Use `docker-compose -f docker-compose.yml` for production
- Configure environment variables

### Learn More
- 📖 [Backend README](./backend/README.md)
- 📖 [Frontend README](./frontend/README.md)
- 📖 [Deployment Guide](./DEPLOYMENT.md)
- 📖 [Main README](./README.md)

## Features Ready to Use

- ✅ Beautiful animated website with motion graphics
- ✅ Intelligent COLLEXA chat agent
- ✅ Student authentication system
- ✅ Appointment booking
- ✅ Seat management
- ✅ Program registration
- ✅ Result checking
- ✅ RAG-powered knowledge base

## Architecture Overview

```
┌─────────────────────────────────────────────┐
│         Browser (http://localhost:3000)     │
│      Next.js Frontend + Motion Graphics     │
└────────────────┬────────────────────────────┘
                 │ HTTP/WebSocket
                 ▼
┌─────────────────────────────────────────────┐
│    FastAPI Backend (http://localhost:8000)  │
│  - Authentication & JWT                      │
│  - COLLEXA Agent (LangGraph)                 │
│  - REST API Endpoints                        │
└────────────────┬────────────────────────────┘
                 │ SQL
        ┌────────┴────────┐
        ▼                 ▼
   PostgreSQL      ChromaDB (RAG)
   (Relational)    (Vector Store)
```

## Getting Help

- 📧 Support: support@kec.edu.np
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

---

**Happy Building! 🎓✨**

Questions? Read the detailed documentation in the project folders!
