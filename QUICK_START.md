# 🚀 COLLEXA - Quick Start Guide

## What's New (Latest Build)

✅ **Professional Warm Color Scheme**
- Warm gold/tan primary colors (inspired by educational institutions)
- Rich professional blues and bronzes
- No generic AI-bot blue/purple colors
- Elegant warm grays for backgrounds

✅ **Amazing Motion Graphics**
- Flying drone animation on landing page
- Drone follows scroll position
- Scroll-triggered content animations
- Smooth page transitions
- Floating and drift animations

✅ **Fixed Chat Agent**
- Better error handling with user-friendly messages
- Helpful debugging tips
- Proper connection status
- Smooth message animations

---

## Quick Start (3 Steps)

### Option A: Automatic Startup (Recommended)

```bash
cd /home/program/Documents/Tutor/VibeCode
./start.sh
```

Then open:
- **Website:** http://localhost:3000
- **API Docs:** http://localhost:8000/api/docs
- **Chat:** Click the bottom-right button on the website

---

### Option B: Manual Startup

**Terminal 1 - Backend:**
```bash
cd /home/program/Documents/Tutor/VibeCode/backend
python3 main.py
```

**Terminal 2 - Frontend:**
```bash
cd /home/program/Documents/Tutor/VibeCode/frontend
npm run dev
```

---

## Current Status

| Component | Status | URL |
|-----------|--------|-----|
| **Frontend (Next.js)** | ✅ Ready | http://localhost:3000 |
| **Backend (FastAPI)** | ✅ Ready | http://localhost:8000 |
| **API Docs** | ✅ Ready | http://localhost:8000/api/docs |
| **Chat Agent** | ✅ Fixed | Bottom-right button |
| **Database** | ✅ SQLite | ./backend/collexa.db |

---

## Features Implemented

### Frontend
- ✈️ Animated hero with flying drone
- 🎨 Warm professional color scheme
- 📱 Fully responsive design
- 💬 Improved chat widget
- 🎬 Scroll animations
- 🌙 Dark mode support

### Backend
- 🤖 Intelligent chat agent
- 📚 RAG system ready
- 🔐 JWT authentication framework
- 📊 Student data models
- 🎓 Program management

### Motion Graphics
- Drone flight animation
- Scroll-following effects
- Content fade-in animations
- Loading pulse animations
- Smooth transitions

---

## Troubleshooting

### "Failed to fetch" error on chat
1. Make sure backend is running: `http://localhost:8000/api/health`
2. Check backend logs: `tail -f /tmp/collexa-backend.log`
3. Restart backend: `python3 backend/main.py`

### Frontend not starting
1. Install dependencies: `cd frontend && npm install`
2. Build: `npm run build`
3. Start: `npm run dev`

### Backend errors
1. Check Python version: `python3 --version` (need 3.8+)
2. Install dependencies: `pip3 install fastapi uvicorn sqlalchemy`
3. Check logs: `/tmp/collexa-backend.log`

---

## Next Steps

1. **Run the app** using `./start.sh`
2. **Test the chat** - Ask COLLEXA about programs
3. **Explore the UI** - Check out animations while scrolling
4. **Check the API** - Visit http://localhost:8000/api/docs
5. **Review code** - Everything is well-commented

---

## Project Structure

```
VibeCode/
├── frontend/              # Next.js 14 React app
│   ├── src/
│   │   ├── app/          # Pages and layouts
│   │   ├── components/   # React components
│   │   │   ├── ChatWidget.tsx       ✨ Fixed chat
│   │   │   ├── HeroSection.tsx      ✈️ Drone animation
│   │   │   ├── Navigation.tsx       🎨 Warm colors
│   │   │   └── ...
│   ├── tailwind.config.js  # 🎨 New color scheme
│   └── package.json
│
├── backend/              # FastAPI Python app
│   ├── main.py           # App entry point
│   ├── agent.py          # 🤖 Chat agent
│   ├── models.py         # Database models
│   ├── routers/          # API endpoints
│   │   ├── chat.py       # Chat endpoint
│   │   ├── auth.py       # Authentication
│   │   └── ...
│   └── pyproject.toml
│
├── start.sh             # 🚀 Easy startup script
└── README.md
```

---

## Color Palette Reference

**Primary (Warm Gold):** `#d4a574`
**Secondary (Bronze):** `#c4a882`
**Accent (Professional Blue):** `#4a6fa5`
**Background (Warm Gray):** `#faf9f7` (light) / `#27231f` (dark)

---

## Commands Reference

```bash
# Start everything
./start.sh

# Start backend only
cd backend && python3 main.py

# Start frontend only
cd frontend && npm run dev

# Build frontend
cd frontend && npm run build

# View frontend logs
tail -f /tmp/collexa-frontend.log

# View backend logs
tail -f /tmp/collexa-backend.log

# Check API health
curl http://localhost:8000/api/health

# View API documentation
# Open: http://localhost:8000/api/docs
```

---

## What's Working

✅ Professional warm color scheme
✅ Animated drone on hero section
✅ Scroll-triggered animations
✅ Chat widget with error handling
✅ Backend API structure
✅ Database models
✅ JWT authentication framework
✅ Dark mode support
✅ Responsive design
✅ Git integration
✅ Docker compose ready

---

## Known Issues & Next Steps

⏳ **Backend dependencies:** Some heavy ML packages may need additional setup
⏳ **RAG system:** Ready to integrate KEC documents
⏳ **Student authentication:** JWT framework in place, login UI needed
⏳ **Admin dashboard:** Ready to build

---

**Happy coding! 🚀 Let me know if you need help with anything!**
