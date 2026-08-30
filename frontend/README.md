# COLLEXA Frontend - Professional Next.js Website

Beautiful, interactive Next.js 14 frontend for KEC with motion graphics powered by Framer Motion.

## Features

- ⚡ **Next.js 14** with TypeScript and App Router
- 🎨 **Motion Graphics** with Framer Motion animations
- 🌙 **Dark Mode** support with dynamic theme switching
- 📱 **Fully Responsive** design with Tailwind CSS
- 🤖 **COLLEXA Chat Widget** - embedded AI assistant
- 🎯 **Interactive Components** with smooth animations
- 🔐 **Authentication** - JWT-based login/register
- 📊 **Real-time Data** - streaming chat responses

## Project Structure

```
frontend/
├── src/
│   ├── app/              # Next.js App Router
│   │   ├── layout.tsx
│   │   ├── page.tsx      # Home page
│   │   ├── globals.css
│   │   └── providers.tsx
│   ├── components/       # Reusable React components
│   │   ├── ChatWidget.tsx
│   │   ├── Hero.tsx
│   │   ├── ProgramsShowcase.tsx
│   │   ├── CampusInfo.tsx
│   │   └── AnimatedBackground.tsx
│   ├── lib/
│   │   └── api.ts        # API client
│   ├── store/
│   │   └── index.ts      # Zustand stores (Auth, Chat)
│   └── types/            # TypeScript types
├── public/               # Static assets
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.js
```

## Installation

```bash
npm install
```

## Environment Setup

Create `.env.local`:

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

## Build

```bash
npm run build
npm start
```

## Key Components

### ChatWidget
- Floating chat bubble with smooth animations
- Real-time message streaming
- Session-based conversation history
- Responsive design for all devices

### Hero Section
- Animated gradient text
- Smooth page transitions
- Call-to-action buttons with hover effects
- Floating animated elements

### Program Cards
- Hover animations with parallax
- Gradient backgrounds
- Responsive grid layout
- Interactive buttons

### AnimatedBackground
- Animated gradient orbs
- Grid pattern overlay
- Smooth color transitions
- Performance optimized

## Animation Libraries

- **Framer Motion** - Advanced animations and interactions
- **Tailwind CSS** - Utility-first styling
- **Zustand** - State management
- **Axios** - HTTP client

## Deployment

### Vercel (Recommended)

```bash
vercel
```

### Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## Performance Tips

- Images are optimized with Next.js Image component
- CSS animations use GPU acceleration (transform, opacity)
- Smooth scrolling enabled
- Dark mode prevents flashing
- Motion reduced for users with preferences

## Support

For issues or questions, please contact the development team.
