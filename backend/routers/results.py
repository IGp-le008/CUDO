"""Student results router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from schemas import StudentResultsResponse, StudentResultResponse
from database import get_async_session
from auth import get_current_user
from models import StudentResult, User

router = APIRouter()


@router.get("/my-results", response_model=StudentResultsResponse)
async def get_my_results(
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Get current student's results."""

    # Get user registration number
    result = await session.execute(
        select(User).where(User.id == UUID(current_user))
    )
    user = result.scalar_one_or_none()

    if not user or not user.registration_number:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student registration number not found"
        )

    # Get results for this student
    results = await session.execute(
        select(StudentResult).where(StudentResult.student_id == user.registration_number)
    )
    student_results = results.scalars().all()

    return {
        "student_id": user.registration_number,
        "results": [
            {
                "semester": res.semester,
                "course_name": res.course_name,
                "course_id": res.course_id,
                "grade": res.grade,
                "marks": res.marks,
                "gpa": res.gpa,
                "published_at": res.published_at
            }
            for res in student_results
        ]
    }


@router.get("/{student_id}", response_model=StudentResultsResponse)
async def get_student_results(
    student_id: str,
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Get results for a specific student (admin only)."""

    # Check if current user is admin
    result = await session.execute(
        select(User).where(User.id == UUID(current_user))
    )
    user = result.scalar_one_or_none()

    if not user or not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    # Get results
    results = await session.execute(
        select(StudentResult).where(StudentResult.student_id == student_id)
    )
    student_results = results.scalars().all()

    return {
        "student_id": student_id,
        "results": [
            {
                "semester": res.semester,
                "course_name": res.course_name,
                "course_id": res.course_id,
                "grade": res.grade,
                "marks": res.marks,
                "gpa": res.gpa,
                "published_at": res.published_at
            }
            for res in student_results
        ]
    }
