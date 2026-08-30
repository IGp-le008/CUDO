# COLLEXA - Comprehensive Project README

🎓 **COLLEXA** - Intelligent AI-Powered Assistant for Kathmandu Engineering College

---

## 📋 Project Overview

COLLEXA is a professional full-stack web application combining:

- **🤖 Intelligent Chat Agent** - LangGraph-powered AI with multi-step reasoning
- **🎨 Beautiful Frontend** - Next.js 14 with Framer Motion animations
- **⚡ Robust Backend** - FastAPI with PostgreSQL + pgvector
- **📚 RAG System** - ChromaDB vector database for knowledge retrieval
- **🔐 Authentication** - JWT-based secure auth system
- **📱 Responsive Design** - Works seamlessly on all devices

---

## 🏗️ Architecture

```
COLLEXA
├── Frontend (Next.js 14)
│   ├── Motion Graphics (Framer Motion)
│   ├── Chat Widget Component
│   ├── Program Showcase
│   └── Campus Information
├── Backend (FastAPI)
│   ├── Authentication & JWT
│   ├── COLLEXA Agent (LangGraph)
│   ├── RAG System (ChromaDB)
│   ├── REST API Endpoints
│   └── Database (PostgreSQL + pgvector)
└── Infrastructure
    ├── Docker Compose
    ├── Database
    └── Vector Store
```

---

## ✨ Key Features

### For Students & Visitors
- 🤖 Ask COLLEXA anything about the college
- 📊 Check admission requirements
- 🎯 View program details
- 🗓️ Book faculty appointments
- 🛑 Reserve seats
- 📝 Register for programs
- 📈 Check academic results

### For Administration
- 👥 Manage student records
- 📢 Post notices and announcements
- 🎓 Update program information
- 📊 View analytics
- 🔧 System configuration

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Git
- Google Gemini API Key

### Local Setup (5 minutes)

```bash
# Clone repo
git clone <repo-url>
cd VibeCode

# Create environment file
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# Start all services
docker-compose up -d

# Access:
# Frontend: http://localhost:3000
# Backend: http://localhost:8000/api/docs
```

---

## 📁 Project Structure

```
VibeCode/
├── frontend/                 # Next.js frontend application
│   ├── src/
│   │   ├── app/             # App Router
│   │   ├── components/      # React components
│   │   ├── lib/             # Utilities & API client
│   │   └── store/           # Zustand state management
│   ├── package.json
│   └── tailwind.config.ts
├── backend/                  # FastAPI backend
│   ├── main.py              # App entry point
│   ├── agent.py             # COLLEXA agent logic
│   ├── models.py            # Database models
│   ├── schemas.py           # Request/Response schemas
│   ├── routers/             # API route handlers
│   │   ├── auth.py
│   │   ├── chat.py
│   │   ├── appointments.py
│   │   ├── seats.py
│   │   ├── registrations.py
│   │   └── results.py
│   ├── rag_system.py        # RAG implementation
│   ├── database.py          # Database connection
│   ├── config.py            # Configuration
│   └── pyproject.toml       # Dependencies
├── docker-compose.yml       # Container orchestration
├── DEPLOYMENT.md            # Deployment guide
└── README.md               # This file
```

---

## 🔧 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js 14, React 18, TypeScript | Modern web UI |
| **Styling** | Tailwind CSS, Framer Motion | Responsive design + animations |
| **State** | Zustand | Client state management |
| **Backend** | FastAPI, Python 3.11 | REST API & business logic |
| **Agent** | LangGraph, LangChain | AI reasoning & tool calling |
| **LLM** | Google Gemini API | Language model |
| **Database** | PostgreSQL + pgvector | Relational data + vectors |
| **Vector DB** | ChromaDB | Semantic search |
| **Auth** | JWT, passlib | Security |
| **Infra** | Docker, Docker Compose | Containerization |

---

## 📚 API Documentation

Once running, view interactive docs at: `http://localhost:8000/api/docs`

### Key Endpoints

**Authentication**
- `POST /api/auth/register` - Create account
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Current user

**Chat**
- `POST /api/chat/query` - Send message to COLLEXA
- `GET /api/chat/history/{session_id}` - Chat history

**Information**
- `GET /api/seats/availability` - Program seat info
- `POST /api/seats/reserve` - Reserve seat
- `POST /api/registrations` - Register for program
- `GET /api/results/my-results` - Academic results

**Appointments**
- `POST /api/appointments` - Book appointment
- `GET /api/appointments` - My appointments

---

## 🤖 COLLEXA Agent Capabilities

The intelligent agent can:

1. **Classify Intent** - Understand what user is asking
2. **Route Queries** - Direct to appropriate tool
3. **Access Tools** - Call backend APIs, RAG system
4. **Generate Responses** - Use LLM for natural language
5. **Handle Multi-step** - Complex workflows with confirmation
6. **Manage Authentication** - Securely handle sensitive operations

### Supported Intents

- General information queries
- Admission process questions
- Program details
- Seat availability
- Student results (authenticated)
- Appointment booking
- Registration
- Admin operations

---

## 🎨 Frontend Features

### Components

- **ChatWidget** - Floating chat bubble with animations
- **Hero** - Animated landing section
- **ProgramsShowcase** - Interactive program cards
- **CampusInfo** - Campus statistics and contact
- **AnimatedBackground** - Gradient orbs and patterns

### Motion Graphics

- Smooth page transitions
- Hover animations on cards
- Floating elements
- Gradient text animations
- Responsive to dark mode

---

## 🔐 Security

- JWT token-based authentication
- Password hashing with bcrypt
- CORS protection
- SQL injection prevention (SQLAlchemy ORM)
- Rate limiting ready
- Secure headers
- Input validation with Pydantic

---

## 📊 Deployment Options

### Development
```bash
docker-compose up
```

### Production
See `DEPLOYMENT.md` for:
- Vercel + Railway
- AWS (ECS + RDS)
- Google Cloud Run
- Docker Swarm

### Key Considerations
- Database backups
- SSL/TLS certificates
- Environment variables
- Monitoring & logging
- Auto-scaling setup

---

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

---

## 📈 Performance

- Next.js optimized images
- CSS-in-JS with Tailwind
- Database indexing
- Vector similarity search
- Async processing
- Connection pooling

---

## 🐛 Troubleshooting

### Container issues
```bash
docker-compose logs -f
docker-compose down
docker-compose up --build
```

### Database connection
```bash
# Check PostgreSQL
docker exec collexa-db psql -U collexa -d collexa_db -c "\dt"
```

### Frontend not loading
```bash
npm install
npm run build
```

---

## 📝 Development Workflow

1. Create branch: `git checkout -b feature/my-feature`
2. Make changes and commit
3. Push branch: `git push origin feature/my-feature`
4. Create pull request
5. Review and merge

---

## 📜 License

[Add your license here]

---

## 👥 Team & Support

For issues or questions:
- 📧 Email: support@kec.edu.np
- 💬 Discord: [Add link]
- 🐛 Issues: GitHub Issues

---

## 🎯 Roadmap

- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] Video tutorials
- [ ] Multi-language support
- [ ] Payment gateway integration
- [ ] Document management system
- [ ] Email notifications
- [ ] SMS integration

---

**Built with ❤️ for Kathmandu Engineering College**
