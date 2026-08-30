"""Deployment guide for COLLEXA."""

# COLLEXA Deployment Guide

## Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Google Gemini API Key
- Domain name (for production)
- SSL certificate (for production)

## Local Development

### 1. Clone Repository
```bash
git clone <repo-url>
cd VibeCode
```

### 2. Environment Setup

Create `.env` in root:
```bash
GOOGLE_API_KEY=your-api-key
SECRET_KEY=your-secret-key
```

### 3. Start with Docker Compose

```bash
docker-compose up -d
```

This will:
- Start PostgreSQL database
- Start FastAPI backend (8000)
- Start Next.js frontend (3000)
- Initialize databases

### 4. Access Services

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

## Production Deployment

### Option 1: Vercel + Railway

**Frontend (Vercel):**
1. Push code to GitHub
2. Connect repo to Vercel
3. Set environment variables
4. Deploy

**Backend (Railway):**
1. Create Railway account
2. Add PostgreSQL plugin
3. Add Python app
4. Link GitHub repo
5. Set environment variables
6. Deploy

### Option 2: AWS (ECS + RDS + CloudFront)

**Database:**
```bash
# Create RDS PostgreSQL instance
# Enable pgvector extension
```

**Backend (ECS):**
1. Create ECR repository
2. Build Docker image: `docker build -t collexa-backend ./backend`
3. Push: `docker push <ecr-url>/collexa-backend`
4. Create ECS task definition
5. Create ECS service
6. Set ALB security groups

**Frontend (CloudFront + S3):**
```bash
npm run build
# Upload to S3
# Create CloudFront distribution
```

### Option 3: Google Cloud Run

**Build image:**
```bash
docker build -t collexa-backend ./backend
docker tag collexa-backend gcr.io/PROJECT_ID/collexa-backend
docker push gcr.io/PROJECT_ID/collexa-backend
```

**Deploy:**
```bash
gcloud run deploy collexa-backend \
  --image gcr.io/PROJECT_ID/collexa-backend \
  --platform managed \
  --region us-central1 \
  --set-env-vars DATABASE_URL=postgresql://...
```

## Database Migrations

```bash
# Inside backend container
alembic upgrade head
```

## Initial Data Setup

```bash
# Load knowledge base
python scripts/load_knowledge_base.py

# Create sample users
python scripts/create_sample_users.py
```

## Monitoring & Logging

### Logs
```bash
# Docker logs
docker-compose logs -f backend

# Check specific service
docker-compose logs backend -f
```

### Database Backup
```bash
# Backup
pg_dump -h localhost -U collexa collexa_db > backup.sql

# Restore
psql -h localhost -U collexa collexa_db < backup.sql
```

### Performance Monitoring
- Use Sentry for error tracking (optional)
- Set up CloudWatch/GCP Monitoring
- Monitor database queries

## Security Checklist

- [ ] Change all default passwords
- [ ] Enable HTTPS/TLS
- [ ] Set CORS properly
- [ ] Enable CSRF protection
- [ ] Implement rate limiting
- [ ] Set up WAF (Web Application Firewall)
- [ ] Regular security audits
- [ ] Keep dependencies updated
- [ ] Enable database encryption
- [ ] Use environment variables for secrets

## Scaling Considerations

1. **Database**: Use read replicas for scaling reads
2. **Backend**: Use auto-scaling with load balancer
3. **Frontend**: Use CDN (CloudFront/Cloudflare)
4. **Caching**: Implement Redis for session/cache layer
5. **Job Queue**: Use Celery for async tasks

## Support & Troubleshooting

For issues, check:
1. Container logs: `docker-compose logs`
2. Database connectivity
3. API health: `curl http://localhost:8000/api/health`
4. Frontend console for errors
5. Network connectivity between services
