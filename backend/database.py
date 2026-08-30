"""Database connection and session management."""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from config import get_settings

settings = get_settings()
Base = declarative_base()

_engine = None
_session_factory = None


def get_async_engine():
    """Return the shared async database engine."""
    global _engine
    if _engine is None:
        _engine = create_async_engine(settings.database_url, echo=settings.database_echo, future=True)
    return _engine


def get_session_factory():
    """Return the shared session factory without creating a new connection pool per request."""
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(get_async_engine(), class_=AsyncSession, expire_on_commit=False)
    return _session_factory


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async database session."""
    async with get_session_factory()() as session:
        try:
            yield session
        finally:
            await session.close()


@asynccontextmanager
async def get_db_session():
    """Context manager for database session."""
    async with get_session_factory()() as session:
        try:
            yield session
        finally:
            await session.close()


async def init_db():
    """Initialize database tables."""
    engine = get_async_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    """Drop all database tables (development only)."""
    if not settings.is_development:
        raise RuntimeError("Cannot drop database in production!")

    engine = get_async_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
