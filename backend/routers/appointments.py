"""Authenticated appointment booking endpoints."""

from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth import get_current_user
from database import get_async_session
from models import Appointment
from schemas import AppointmentCreate, AppointmentResponse

router = APIRouter()


@router.post("/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
async def create_appointment(
    appointment_data: AppointmentCreate,
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    if appointment_data.scheduled_time <= datetime.now(timezone.utc).replace(tzinfo=None):
        raise HTTPException(status_code=400, detail="Appointments must be scheduled in the future")

    appointment = Appointment(student_id=UUID(current_user), **appointment_data.model_dump())
    session.add(appointment)
    await session.commit()
    await session.refresh(appointment)
    return appointment


@router.get("/", response_model=list[AppointmentResponse])
async def get_my_appointments(
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(Appointment)
        .where(Appointment.student_id == UUID(current_user))
        .order_by(Appointment.scheduled_time)
    )
    return result.scalars().all()


@router.post("/{appointment_id}/cancel", response_model=AppointmentResponse)
async def cancel_appointment(
    appointment_id: UUID,
    current_user: str = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    appointment = await session.scalar(select(Appointment).where(Appointment.id == appointment_id))
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    if appointment.student_id != UUID(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to cancel this appointment")
    if appointment.status in {"cancelled", "completed"}:
        raise HTTPException(status_code=400, detail="Appointment cannot be cancelled")
    appointment.status = "cancelled"
    await session.commit()
    await session.refresh(appointment)
    return appointment
