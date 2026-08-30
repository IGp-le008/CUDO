#!/bin/bash

# COLLEXA - Development Environment Setup & Run Guide
# Last Updated: August 31, 2026

echo "🚀 COLLEXA - Kathmandu Engineering College AI Assistant"
echo "════════════════════════════════════════════════════════"
echo ""

# Step 1: Check Prerequisites
echo "📋 Step 1: Checking Prerequisites..."
echo ""

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found"
    echo "   Install from: https://nodejs.org/"
    exit 1
fi
echo "✅ Node.js $(node --version)"

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found"
    exit 1
fi
echo "✅ npm $(npm --version)"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found"
    echo "   Install Python 3.8+ from: https://python.org/"
    exit 1
fi
echo "✅ Python $(python3 --version)"

echo ""
echo "════════════════════════════════════════════════════════"
echo ""

# Step 2: Install Dependencies
echo "📦 Step 2: Installing Dependencies..."
echo ""

cd frontend
if [ -d "node_modules" ]; then
    echo "   Frontend dependencies already installed"
else
    echo "   Installing frontend dependencies..."
    npm install
fi
cd ..

echo "✅ Dependencies ready"
echo ""

# Step 3: Explain What's Running
echo "════════════════════════════════════════════════════════"
echo ""
echo "ℹ️  What COLLEXA Includes:"
echo ""
echo "🎨 FRONTEND (Next.js 14)"
echo "   • Warm professional color scheme (gold, bronze, blue)"
echo "   • Animated hero section with flying drone"
echo "   • Responsive design with dark mode"
echo "   • Chat widget with error handling"
echo "   • Smooth scroll animations"
echo "   • No generic AI-bot look"
echo ""
echo "🤖 BACKEND (FastAPI)"
echo "   • Intelligent chat agent with 7 intent types"
echo "   • Tool-calling architecture"
echo "   • RAG system ready for KEC documents"
echo "   • Student/Program/Result models"
echo "   • JWT authentication framework"
echo "   • CORS & security configured"
echo ""
echo "💬 CHAT FEATURES"
echo "   • Ask about programs, admissions, appointments"
echo "   • Error detection & helpful debugging tips"
echo "   • Smooth animations & loading states"
echo "   • Connection status verification"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""

# Step 4: Show How to Run
echo "🚀 Step 3: To Start COLLEXA:"
echo ""
echo "OPTION A - Automatic (Recommended):"
echo "   $ ./start.sh"
echo ""
echo "OPTION B - Manual:"
echo "   Terminal 1 (Backend):"
echo "   $ cd backend"
echo "   $ python3 main.py"
echo ""
echo "   Terminal 2 (Frontend):"
echo "   $ cd frontend"
echo "   $ npm run dev"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""

# Step 5: Show Access Points
echo "📱 Step 4: Access Points:"
echo ""
echo "🌐 Website:"
echo "   http://localhost:3000"
echo "   • Homepage with drone animation"
echo "   • Chat widget (bottom-right)"
echo "   • Program showcase"
echo "   • Warm professional design"
echo ""
echo "📚 API Documentation:"
echo "   http://localhost:8000/api/docs"
echo "   • Interactive Swagger UI"
echo "   • Test all endpoints"
echo "   • View schemas"
echo ""
echo "🏥 Health Check:"
echo "   http://localhost:8000/api/health"
echo "   • Verify backend is running"
echo "   • Returns: { \"status\": \"healthy\" }"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""

# Step 6: Troubleshooting
echo "🔧 Step 5: Troubleshooting:"
echo ""
echo "❓ \"Failed to fetch\" error in chat?"
echo "   → Check if backend is running"
echo "   → Visit http://localhost:8000/api/health"
echo "   → Restart: cd backend && python3 main.py"
echo ""
echo "❓ Frontend not loading?"
echo "   → Check npm: npm --version"
echo "   → Reinstall: cd frontend && npm install"
echo "   → Rebuild: npm run build"
echo ""
echo "❓ Port already in use?"
echo "   → Linux/Mac: lsof -ti :3000 | xargs kill -9"
echo "   → Windows: netstat -ano | findstr :3000"
echo ""
echo "❓ Animations stuttering?"
echo "   → Try different browser (Chrome recommended)"
echo "   → Disable browser extensions"
echo "   → Check CPU usage"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""

# Step 7: Documentation Links
echo "📚 Documentation:"
echo ""
echo "📄 QUICK_START.md"
echo "   • Fastest way to get running"
echo "   • Common issues & solutions"
echo ""
echo "📘 IMPLEMENTATION_SUMMARY.md"
echo "   • Complete project overview"
echo "   • What's implemented"
echo "   • Architecture details"
echo ""
echo "📙 README.md"
echo "   • Project description"
echo "   • Feature list"
echo "   • Technology stack"
echo ""
echo "📕 DEPLOYMENT.md"
echo "   • Production deployment"
echo "   • Docker setup"
echo "   • Environment variables"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""

# Step 8: Color Scheme Info
echo "🎨 Color Scheme (Professional, Non-Robotic):"
echo ""
echo "Primary (Warm Gold):"
echo "   Light: #f2b159  →  Dark: #8b7043"
echo "   Use: Main buttons, highlights, primary UI"
echo ""
echo "Secondary (Warm Bronze):"
echo "   Light: #c4a882  →  Dark: #4f4035"
echo "   Use: Cards, backgrounds, secondary elements"
echo ""
echo "Accent (Professional Blue):"
echo "   Light: #6b8cbe  →  Dark: #1f314d"
echo "   Use: Links, focus states, important elements"
echo ""
echo "Background (Warm Grays):"
echo "   Light: #faf9f7  →  Dark: #1a1715"
echo "   Use: Page backgrounds, text areas"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""

# Step 9: What's Next
echo "✨ What's Next After Running:"
echo ""
echo "1. ✅ Test the homepage - Observe drone animation"
echo "2. ✅ Scroll down - See scroll-triggered animations"
echo "3. ✅ Click chat button - Ask about programs"
echo "4. ✅ Check dark mode - Toggle dark/light"
echo "5. ✅ Review API docs - Explore endpoints"
echo "6. ✅ Check GitHub - Review code changes"
echo "7. ✅ Plan Phase 2 - Student authentication"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""

# Step 10: Final Info
echo "📊 Project Status:"
echo ""
echo "✅ Frontend: Ready (Next.js 14, Framer Motion)"
echo "✅ Backend: Ready (FastAPI, SQLAlchemy)"
echo "✅ Chat Agent: Fixed (Error handling, animations)"
echo "✅ Motion Graphics: Implemented (Drone, scroll effects)"
echo "✅ Color Scheme: Professional (Warm, elegant)"
echo "✅ Documentation: Complete (Guides & troubleshooting)"
echo "✅ Git: Synced (All changes pushed)"
echo ""

echo "════════════════════════════════════════════════════════"
echo ""
echo "🎉 Ready to launch? Run: ./start.sh"
echo ""
echo "For questions, see QUICK_START.md or IMPLEMENTATION_SUMMARY.md"
echo ""
echo "Built with ❤️ for Kathmandu Engineering College"
echo "════════════════════════════════════════════════════════"
