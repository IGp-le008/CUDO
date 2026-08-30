"""Main FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config import get_settings
from routers import auth, chat, appointments, seats, registrations, results

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for app startup/shutdown."""
    # Startup
    print("🚀 COLLEXA Backend Starting...")

    yield

    # Shutdown
    print("🛑 COLLEXA Backend Shutting Down...")


# Create FastAPI app
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description,
    lifespan=lifespan,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(appointments.router, prefix="/api/appointments", tags=["Appointments"])
app.include_router(seats.router, prefix="/api/seats", tags=["Seats"])
app.include_router(registrations.router, prefix="/api/registrations", tags=["Registrations"])
app.include_router(results.router, prefix="/api/results", tags=["Results"])


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "COLLEXA Backend",
        "version": settings.api_version
    }


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to COLLEXA",
        "docs": "/api/docs",
        "health": "/api/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.is_development,
    )
