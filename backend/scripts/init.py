"""Backend initialization script."""

import asyncio
import logging
import sys
from pathlib import Path

# Add backend root to path so imports work when this script is run directly
BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def initialize_backend():
    """Initialize backend - create tables and load data."""
    logger.info("🚀 Initializing COLLEXA Backend...")

    try:
        logger.info("📦 Creating database tables...")
        await init_db()
        logger.info("✅ Database tables created")

        logger.info("📚 Loading knowledge base...")
        from scripts.load_knowledge_base import load_knowledge_base
        await load_knowledge_base()
        logger.info("✅ Knowledge base loaded")

        logger.info("👥 Creating sample users...")
        from scripts.create_sample_users import create_sample_users
        await create_sample_users()
        logger.info("✅ Sample users created")

        logger.info("✅ Backend initialization complete!")
        logger.info("🎯 You can now start the server with: python main.py")

    except Exception as e:
        logger.error(f"❌ Initialization failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(initialize_backend())
