"""SQLAlchemy ORM models for COLLEXA."""

from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Enum, JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
from enum import Enum as PyEnum

from database import Base


class User(Base):
    """Student/User model."""
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    registration_number = Column(String(50), unique=True, nullable=True, index=True)
    phone = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    appointments = relationship("Appointment", back_populates="student")
    chat_history = relationship("ChatMessage", back_populates="user")
    registrations = relationship("Registration", back_populates="student")

    def __repr__(self):
        return f"<User {self.email}>"


class ChatMessage(Base):
    """Chat message history."""
    __tablename__ = "chat_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    session_id = Column(String(255), index=True)
    role = Column(String(20), nullable=False)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    metadata = Column(JSONB, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    # Relationships
    user = relationship("User", back_populates="chat_history")

    def __repr__(self):
        return f"<ChatMessage {self.id}>"


class Appointment(Base):
    """Faculty appointment booking."""
    __tablename__ = "appointments"

    class StatusEnum(str, PyEnum):
        PENDING = "pending"
        CONFIRMED = "confirmed"
        CANCELLED = "cancelled"
        COMPLETED = "completed"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    faculty_id = Column(String(100), nullable=False)  # Faculty identifier
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String(20), default=StatusEnum.PENDING.value)
    meeting_link = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    student = relationship("User", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment {self.id}>"


class SeatAllocation(Base):
    """Seat availability and allocation."""
    __tablename__ = "seat_allocations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    program_id = Column(String(100), nullable=False, index=True)
    program_name = Column(String(255), nullable=False)
    total_seats = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)
    reserved_seats = Column(Integer, default=0)
    admission_cycle = Column(String(50), nullable=False)  # e.g., "2024-Fall"
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<SeatAllocation {self.program_name}>"


class SeatReservation(Base):
    """Student seat reservations."""
    __tablename__ = "seat_reservations"

    class StatusEnum(str, PyEnum):
        PENDING = "pending"
        CONFIRMED = "confirmed"
        CANCELLED = "cancelled"
        EXPIRED = "expired"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    seat_allocation_id = Column(UUID(as_uuid=True), ForeignKey("seat_allocations.id"))
    program_id = Column(String(100), nullable=False)
    status = Column(String(20), default=StatusEnum.PENDING.value)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    confirmed_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<SeatReservation {self.id}>"


class Registration(Base):
    """Student registration records."""
    __tablename__ = "registrations"

    class StatusEnum(str, PyEnum):
        PENDING = "pending"
        CONFIRMED = "confirmed"
        COMPLETED = "completed"
        CANCELLED = "cancelled"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    program_id = Column(String(100), nullable=False)
    program_name = Column(String(255), nullable=False)
    status = Column(String(20), default=StatusEnum.PENDING.value)
    qr_code = Column(String(500), nullable=True)
    confirmation_code = Column(String(50), unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    confirmed_at = Column(DateTime, nullable=True)

    # Relationships
    student = relationship("User", back_populates="registrations")

    def __repr__(self):
        return f"<Registration {self.confirmation_code}>"


class StudentResult(Base):
    """Student academic results."""
    __tablename__ = "student_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(String(100), nullable=False, index=True)
    semester = Column(String(50), nullable=False)  # e.g., "Fall 2024"
    course_id = Column(String(100), nullable=False)
    course_name = Column(String(255), nullable=False)
    grade = Column(String(5), nullable=True)  # A+, A, B+, B, etc.
    marks = Column(Integer, nullable=True)
    gpa = Column(String(10), nullable=True)
    published_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<StudentResult {self.student_id} - {self.course_name}>"


class KnowledgeBase(Base):
    """RAG Knowledge base documents."""
    __tablename__ = "knowledge_base"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)  # e.g., "admissions", "programs"
    source = Column(String(255), nullable=True)
    embedding_id = Column(String(255), nullable=True)  # ChromaDB reference
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<KnowledgeBase {self.title}>"


class Notice(Base):
    """College notices and announcements."""
    __tablename__ = "notices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)  # e.g., "admission", "academic"
    priority = Column(String(20), default="normal")  # "high", "normal", "low"
    is_active = Column(Boolean, default=True)
    published_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Notice {self.title}>"
