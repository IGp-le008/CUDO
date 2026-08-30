"""Small, deterministic retrieval layer for approved KEC knowledge-base content.

This keeps public answers grounded even when an optional external LLM is unavailable.
"""

from collections import Counter
import re

from knowledge_base import get_knowledge_base


class RAGSystem:
    def __init__(self):
        self.documents = list(get_knowledge_base())

    def add_document(self, doc_id: str, content: str, metadata: dict | None = None):
        """Add or replace a document in the in-memory knowledge store."""
        doc = {
            "id": doc_id,
            "title": metadata.get("title", "Untitled") if metadata else "Untitled",
            "content": content,
            "category": metadata.get("category", "general") if metadata else "general",
            "source": metadata.get("source") if metadata else None,
        }
        existing_index = next((i for i, item in enumerate(self.documents) if item.get("id") == doc_id), None)
        if existing_index is not None:
            self.documents[existing_index] = doc
        else:
            self.documents.append(doc)

    def get_relevant_context(self, query: str, limit: int = 3) -> str:
        if not query or not self.documents:
            return ""

        query_tokens = set(re.findall(r"[a-z0-9]+", query.lower()))
        ranked: list[tuple[int, str]] = []
        for document in self.documents:
            text = f"{document.get('title', '')} {document.get('content', '')}"
            document_tokens = re.findall(r"[a-z0-9]+", text.lower())
            score = sum(Counter(document_tokens)[token] for token in query_tokens)
            if score:
                ranked.append((score, text.strip()))
        ranked.sort(key=lambda item: item[0], reverse=True)
        return "\n\n".join(text for _, text in ranked[:limit])


_rag_system = RAGSystem()


def get_rag_system() -> RAGSystem:
    return _rag_system
