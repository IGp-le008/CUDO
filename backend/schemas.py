"""API request and response schemas."""

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=1, max_length=255)
    registration_number: str | None = Field(default=None, max_length=50)
    phone: str | None = Field(default=None, max_length=20)


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    email: EmailStr
    full_name: str
    registration_number: str | None
    phone: str | None
    is_active: bool
    is_admin: bool
    created_at: datetime


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int


class ChatQueryRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2_000)
    session_id: str = Field(min_length=1, max_length=255)
    context: dict[str, Any] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    response: str
    session_id: str
    sources: list[str] = Field(default_factory=list)
    requires_auth: bool = False
    next_action: str | None = None


class ChatMessageResponse(BaseModel):
    id: UUID
    role: Literal["user", "assistant"]
    content: str
    created_at: datetime


class ChatSessionResponse(BaseModel):
    session_id: str
    messages: list[ChatMessageResponse]


class AppointmentCreate(BaseModel):
    faculty_id: str = Field(min_length=1, max_length=100)
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=5_000)
    scheduled_time: datetime


class AppointmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    faculty_id: str
    title: str
    description: str | None
    scheduled_time: datetime
    status: str
    meeting_link: str | None
    created_at: datetime


class SeatAvailabilityResponse(BaseModel):
    program_id: str
    program_name: str
    total_seats: int
    available_seats: int
    reserved_seats: int
    admission_cycle: str


class SeatReservationResponse(BaseModel):
    id: UUID
    program_id: str
    status: str
    created_at: datetime
    expires_at: datetime | None


class RegistrationCreate(BaseModel):
    program_id: str = Field(min_length=1, max_length=100)
    user_confirmation: bool


class RegistrationResponse(BaseModel):
    id: UUID
    program_id: str
    program_name: str
    status: str
    confirmation_code: str | None
    qr_code: str | None
    created_at: datetime
    confirmed_at: datetime | None


class StudentResultResponse(BaseModel):
    semester: str
    course_name: str
    course_id: str
    grade: str | None
    marks: int | None
    gpa: str | None
    published_at: datetime


class StudentResultsResponse(BaseModel):
    student_id: str
    results: list[StudentResultResponse]
