"""Chat router for COLLEXA agent."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from schemas import ChatQueryRequest, ChatResponse, ChatSessionResponse
from database import get_async_session
from rag_system import get_rag_system
from models import ChatMessage

router = APIRouter()


@router.post("/query", response_model=ChatResponse)
async def chat_query(
    request: ChatQueryRequest,
    session: AsyncSession = Depends(get_async_session)
):
    """Process a chat query through COLLEXA agent."""

    rag = get_rag_system()

    # Get relevant context from knowledge base
    context = rag.get_relevant_context(request.query)

    # Save user message to history
    user_message = ChatMessage(
        session_id=request.session_id,
        user_id=None,
        role="user",
        content=request.query,
        metadata=request.context
    )
    session.add(user_message)
    await session.commit()

    # TODO: Integrate with COLLEXA agent (LangGraph)
    # For now, return a basic response
    response_content = context or (
        "I could not find that in the approved KEC knowledge base. "
        "Please contact KEC administration for verified information."
    )

    # Save assistant message to history
    assistant_message = ChatMessage(
        session_id=request.session_id,
        user_id=None,
        role="assistant",
        content=response_content,
        metadata={"source": "rag_system"}
    )
    session.add(assistant_message)
    await session.commit()

    return ChatResponse(
        response=response_content,
        session_id=request.session_id,
        sources=["knowledge_base"],
        requires_auth=False,
        next_action=None
    )


@router.get("/history/{session_id}", response_model=ChatSessionResponse)
async def get_chat_history(
    session_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    """Get chat history for a session."""

    result = await session.execute(
        select(ChatMessage)
        .where(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at)
    )
    messages = result.scalars().all()

    return ChatSessionResponse(
        session_id=session_id,
        messages=[
            {
                "id": msg.id,
                "role": msg.role,
                "content": msg.content,
                "created_at": msg.created_at
            }
            for msg in messages
        ]
    )


@router.delete("/history/{session_id}")
async def clear_chat_history(
    session_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    """Clear chat history for a session."""

    await session.execute(
        delete(ChatMessage).where(ChatMessage.session_id == session_id)
    )
    await session.commit()

    return {"message": "Chat history cleared"}
