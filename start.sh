#!/bin/bash

# COLLEXA Startup Script - Run Frontend and Backend

echo "🚀 Starting COLLEXA Development Environment..."
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python version
echo "${BLUE}[1/4]${NC} Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "${RED}❌ Python3 not found. Please install Python 3.8+${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"
echo ""

# Check Node version
echo "${BLUE}[2/4]${NC} Checking Node.js installation..."
if ! command -v node &> /dev/null; then
    echo "${RED}❌ Node.js not found. Please install Node.js 18+${NC}"
    exit 1
fi
NODE_VERSION=$(node --version)
echo "${GREEN}✓ Node ${NODE_VERSION} found${NC}"
echo ""

# Start Backend
echo "${BLUE}[3/4]${NC} Starting FastAPI Backend..."
cd backend
python3 main.py > /tmp/collexa-backend.log 2>&1 &
BACKEND_PID=$!
echo "${GREEN}✓ Backend started (PID: ${BACKEND_PID})${NC}"
echo "   📝 Logs: /tmp/collexa-backend.log"
echo "   🔗 API Docs: http://localhost:8000/api/docs"
echo ""

# Wait a bit for backend to start
sleep 3

# Check backend health
echo "${YELLOW}Checking backend health...${NC}"
HEALTH=$(curl -s http://localhost:8000/api/health 2>&1)
if echo "$HEALTH" | grep -q "healthy"; then
    echo "${GREEN}✓ Backend is healthy${NC}"
else
    echo "${YELLOW}⚠ Backend may still be initializing...${NC}"
fi
echo ""

# Start Frontend
echo "${BLUE}[4/4]${NC} Starting Next.js Frontend..."
cd ../frontend
npm run dev > /tmp/collexa-frontend.log 2>&1 &
FRONTEND_PID=$!
echo "${GREEN}✓ Frontend started (PID: ${FRONTEND_PID})${NC}"
echo "   📝 Logs: /tmp/collexa-frontend.log"
echo "   🌐 Website: http://localhost:3000"
echo ""

echo "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo "${GREEN}✅ COLLEXA is running!${NC}"
echo ""
echo "${YELLOW}Backend:${NC}"
echo "  • API: http://localhost:8000"
echo "  • Docs: http://localhost:8000/api/docs"
echo "  • Health: http://localhost:8000/api/health"
echo ""
echo "${YELLOW}Frontend:${NC}"
echo "  • Website: http://localhost:3000"
echo "  • Chat: http://localhost:3000 (bottom right)"
echo ""
echo "${YELLOW}To stop:${NC} Press Ctrl+C or run:"
echo "  kill ${BACKEND_PID} ${FRONTEND_PID}"
echo ""
echo "${GREEN}═══════════════════════════════════════════════════════════${NC}"

# Keep script running
wait
