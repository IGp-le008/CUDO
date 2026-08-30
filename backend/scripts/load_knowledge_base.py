"""Initialize and load knowledge base into the in-memory retrieval store."""

import asyncio
import logging
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from knowledge_base import get_knowledge_base
from rag_system import get_rag_system

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def load_knowledge_base():
    """Load sample KEC knowledge base into the retrieval store."""
    logger.info("🚀 Loading knowledge base...")

    rag = get_rag_system()
    kb_items = get_knowledge_base()

    for idx, item in enumerate(kb_items, 1):
        try:
            rag.add_document(
                doc_id=f"kec_{idx}",
                content=item["content"],
                metadata={
                    "title": item["title"],
                    "category": item["category"],
                    "source": "kec_official",
                },
            )
            logger.info(f"✅ Loaded: {item['title']}")
        except Exception as e:
            logger.error(f"❌ Error loading {item['title']}: {e}")

    logger.info(f"✅ Successfully loaded {len(kb_items)} documents")


if __name__ == "__main__":
    asyncio.run(load_knowledge_base())
