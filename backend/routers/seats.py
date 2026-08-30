"""Seat availability and reservation router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timedelta
from uuid import UUID

from schemas import SeatAvailabilityResponse, SeatReservationResponse
from database import get_async_session
from auth import get_current_user
from models import SeatAllocation, SeatReservation

router = APIRouter()


@router.get("/availability", response_model=list[SeatAvailabilityResponse])
async def get_seat_availability(
    session: AsyncSession = Depends(get_async_session)
):
    """Get current seat availability across programs."""

    result = await session.execute(select(SeatAllocation))
    seats = result.scalars().all()

    return [
        {
            "program_id": seat.program_id,
            "program_name": seat.program_name,
            "total_seats": seat.total_seats,
            "available_seats": seat.available_seats,
            "reserved_seats": seat.reserved_seats,
            "admission_cycle": seat.admission_cycle
        }
        for seat in seats
    ]


@router.get("/availability/{program_id}", response_model=SeatAvailabilityResponse)
async def get_program_availability(
    program_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    """Get seat availability for a specific program."""

    result = await session.execute(
        select(SeatAllocation).where(SeatAllocation.program_id == program_id).with_for_update()
    )
    seat = result.scalar_one_or_none()

    if not seat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )

    return {
        "program_id": seat.program_id,
        "program_name": seat.program_name,
        "total_seats": seat.total_seats,
        "available_seats": seat.available_seats,
        "reserved_seats": seat.reserved_seats,
        "admission_cycle": seat.admission_cycle
    }


@router.post("/reserve", response_model=SeatReservationResponse)
async def reserve_seat(
    program_id: str,
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Reserve a seat in a program."""

    # Get seat allocation
    result = await session.execute(
        select(SeatAllocation).where(SeatAllocation.program_id == program_id)
    )
    seat_allocation = result.scalar_one_or_none()

    if not seat_allocation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )

    if seat_allocation.available_seats <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No seats available"
        )

    existing = await session.scalar(
        select(SeatReservation).where(
            SeatReservation.user_id == UUID(current_user),
            SeatReservation.program_id == program_id,
            SeatReservation.status.in_(["pending", "confirmed"]),
        )
    )
    if existing:
        raise HTTPException(status_code=409, detail="You already have an active reservation for this program")

    # Reservations expire to ensure temporarily held seats are released.
    reservation = SeatReservation(
        user_id=UUID(current_user),
        program_id=program_id,
        seat_allocation_id=seat_allocation.id,
        status="pending",
        expires_at=datetime.utcnow() + timedelta(hours=24),
    )

    # Update seat count
    seat_allocation.available_seats -= 1
    seat_allocation.reserved_seats += 1

    session.add(reservation)
    await session.commit()
    await session.refresh(reservation)

    return {
        "id": reservation.id,
        "program_id": reservation.program_id,
        "status": reservation.status,
        "created_at": reservation.created_at,
        "expires_at": reservation.expires_at
    }


@router.get("/my-reservations", response_model=list[SeatReservationResponse])
async def get_my_reservations(
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Get current user's seat reservations."""
    from uuid import UUID

    result = await session.execute(
        select(SeatReservation).where(SeatReservation.user_id == UUID(current_user))
    )
    reservations = result.scalars().all()

    return [
        {
            "id": res.id,
            "program_id": res.program_id,
            "status": res.status,
            "created_at": res.created_at,
            "expires_at": res.expires_at
        }
        for res in reservations
    ]
