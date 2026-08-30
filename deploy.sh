#!/bin/bash

# COLLEXA Deployment Script - Deploy to production

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 COLLEXA Deployment Script${NC}"

# Check environment
if [ ! -f ".env.production" ]; then
    echo -e "${RED}❌ .env.production not found${NC}"
    exit 1
fi

echo -e "${BLUE}📦 Building Docker images...${NC}"
docker-compose -f docker-compose.yml build

echo -e "${BLUE}🗄️  Starting services...${NC}"
docker-compose -f docker-compose.yml up -d

echo -e "${BLUE}⏳ Waiting for services to start...${NC}"
sleep 10

echo -e "${BLUE}🗄️  Running database migrations...${NC}"
docker-compose exec -T backend alembic upgrade head

echo -e "${BLUE}📚 Loading knowledge base...${NC}"
docker-compose exec -T backend python scripts/load_knowledge_base.py

echo -e "${GREEN}✅ Deployment complete!${NC}"
echo -e "${BLUE}📊 Services:${NC}"
echo "  Frontend: http://localhost:3000"
echo "  Backend: http://localhost:8000"
echo "  API Docs: http://localhost:8000/api/docs"
