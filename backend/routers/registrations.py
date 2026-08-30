"""Registrations router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
import secrets

from schemas import RegistrationCreate, RegistrationResponse
from database import get_async_session
from auth import get_current_user
from models import Registration, SeatAllocation, SeatReservation

router = APIRouter()


@router.post("/", response_model=RegistrationResponse)
async def register_program(
    registration_data: RegistrationCreate,
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Register for a program."""

    # Verify user confirmation
    if not registration_data.user_confirmation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User confirmation required"
        )

    seat_reservation = await session.scalar(
        select(SeatReservation).where(
            SeatReservation.user_id == UUID(current_user),
            SeatReservation.program_id == registration_data.program_id,
            SeatReservation.status == "pending",
        ).order_by(SeatReservation.created_at.desc())
    )
    if not seat_reservation:
        raise HTTPException(status_code=400, detail="An active seat reservation is required before registration")
    allocation = await session.scalar(
        select(SeatAllocation).where(SeatAllocation.id == seat_reservation.seat_allocation_id)
    )
    if not allocation:
        raise HTTPException(status_code=400, detail="Reserved program is unavailable")

    # Create registration based on the actual reserved program.
    confirmation_code = secrets.token_hex(8).upper()

    registration = Registration(
        student_id=UUID(current_user),
        program_id=registration_data.program_id,
        program_name=allocation.program_name,
        status="pending",
        confirmation_code=confirmation_code
    )

    session.add(registration)
    await session.commit()
    await session.refresh(registration)

    return {
        "id": registration.id,
        "program_id": registration.program_id,
        "program_name": registration.program_name,
        "status": registration.status,
        "confirmation_code": confirmation_code,
        "qr_code": None,
        "created_at": registration.created_at,
        "confirmed_at": registration.confirmed_at
    }


@router.get("/", response_model=list[RegistrationResponse])
async def get_my_registrations(
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Get current user's registrations."""

    result = await session.execute(
        select(Registration).where(Registration.student_id == UUID(current_user))
    )
    registrations = result.scalars().all()

    return [
        {
            "id": reg.id,
            "program_id": reg.program_id,
            "program_name": reg.program_name,
            "status": reg.status,
            "confirmation_code": reg.confirmation_code,
            "qr_code": reg.qr_code,
            "created_at": reg.created_at,
            "confirmed_at": reg.confirmed_at
        }
        for reg in registrations
    ]


@router.get("/{registration_id}", response_model=RegistrationResponse)
async def get_registration(
    registration_id: UUID,
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Get registration details."""

    result = await session.execute(
        select(Registration).where(Registration.id == registration_id)
    )
    registration = result.scalar_one_or_none()

    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )

    # Check authorization
    if str(registration.student_id) != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view this registration"
        )

    return {
        "id": registration.id,
        "program_id": registration.program_id,
        "program_name": registration.program_name,
        "status": registration.status,
        "confirmation_code": registration.confirmation_code,
        "qr_code": registration.qr_code,
        "created_at": registration.created_at,
        "confirmed_at": registration.confirmed_at
    }


@router.post("/{registration_id}/confirm")
async def confirm_registration(
    registration_id: UUID,
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Confirm a registration."""

    result = await session.execute(
        select(Registration).where(Registration.id == registration_id)
    )
    registration = result.scalar_one_or_none()

    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )

    # Check authorization
    if str(registration.student_id) != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to confirm this registration"
        )

    from datetime import datetime
    if registration.status == "confirmed":
        return {"message": "Registration is already confirmed", "confirmation_code": registration.confirmation_code}
    reservation = await session.scalar(
        select(SeatReservation).where(
            SeatReservation.user_id == UUID(current_user),
            SeatReservation.program_id == registration.program_id,
            SeatReservation.status == "pending",
        ).order_by(SeatReservation.created_at.desc())
    )
    if not reservation:
        raise HTTPException(status_code=400, detail="The associated seat reservation is no longer active")

    registration.status = "confirmed"
    reservation.status = "confirmed"
    registration.confirmed_at = datetime.utcnow()

    await session.commit()

    return {"message": "Registration confirmed"}
