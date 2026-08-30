"""COLLEXA Agent - Intelligent multi-step agent with tool calling."""

from typing import Any, Dict, List, Optional, Annotated
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from enum import Enum
import json
import re

from config import get_settings
from rag_system import get_rag_system

settings = get_settings()


# ============ Agent State ============

class AgentState(BaseModel):
    """State managed by the agent."""
    messages: List[BaseMessage]
    current_user_id: Optional[str] = None
    requires_auth: bool = False
    session_id: str = ""
    context: Dict[str, Any] = Field(default_factory=dict)


# ============ Intent Classifier ============

class IntentType(str, Enum):
    """User intent classification."""
    GENERAL_INFO = "general_info"  # Ask about college info
    ADMISSIONS = "admissions"  # Admissions questions
    PROGRAMS = "programs"  # Program information
    RESULTS = "results"  # Check results
    APPOINTMENTS = "appointments"  # Book appointment
    SEATS = "seats"  # Check seat availability
    REGISTRATION = "registration"  # Register for program
    ADMIN = "admin"  # Admin operations
    UNKNOWN = "unknown"


def classify_intent(query: str) -> IntentType:
    """Classify user intent from query."""
    query_lower = query.lower()

    if any(word in query_lower for word in ["result", "grade", "marks", "score", "cgpa", "sgpa"]):
        return IntentType.RESULTS
    elif any(word in query_lower for word in ["appointment", "meeting", "faculty", "professor"]):
        return IntentType.APPOINTMENTS
    elif any(word in query_lower for word in ["seat", "availability", "seats available"]):
        return IntentType.SEATS
    elif any(word in query_lower for word in ["register", "registration", "admit", "admission"]):
        return IntentType.REGISTRATION
    elif any(word in query_lower for word in ["program", "course", "engineering", "discipline"]):
        return IntentType.PROGRAMS
    elif any(word in query_lower for word in ["admit", "apply", "application", "eligibility"]):
        return IntentType.ADMISSIONS
    elif any(word in query_lower for word in ["admin", "manage", "system"]):
        return IntentType.ADMIN
    else:
        return IntentType.GENERAL_INFO


# ============ Tool Definitions ============

@tool
def search_kec_information(query: str) -> str:
    """Search KEC knowledge base for general information using RAG system."""
    try:
        rag = get_rag_system()
        context = rag.get_relevant_context(query)
        if context:
            return f"From KEC Knowledge Base:\n{context}"
        else:
            return f"No specific information found about '{query}'. Please contact KEC administration for verified information."
    except Exception as e:
        return f"Error searching knowledge base: {str(e)}"


@tool
def get_program_information(program_id: str) -> str:
    """Get detailed information about a specific engineering program."""
    programs = {
        "civil": {
            "name": "Bachelor of Civil Engineering",
            "duration": "4 years",
            "seats": 60,
            "description": "Focus on infrastructure design, construction management, and structural engineering.",
        },
        "computer": {
            "name": "Bachelor of Computer Engineering",
            "duration": "4 years",
            "seats": 65,
            "description": "Study software development, algorithms, databases, and computer networks.",
        },
        "electrical": {
            "name": "Bachelor of Electrical Engineering",
            "duration": "4 years",
            "seats": 50,
            "description": "Learn power systems, electrical machines, and electrical design.",
        },
        "electronics": {
            "name": "Communication, Electronics and IT Engineering",
            "duration": "4 years",
            "seats": 58,
            "description": "Study telecommunications, signal processing, and modern electronics.",
        },
        "architecture": {
            "name": "Bachelor of Architecture",
            "duration": "5 years",
            "seats": 55,
            "description": "Design buildings and urban spaces combining creativity and technical expertise.",
        },
    }

    program = programs.get(program_id.lower())
    if program:
        return (
            f"**{program['name']}**\n"
            f"Duration: {program['duration']}\n"
            f"Available Seats: {program['seats']}\n"
            f"Description: {program['description']}"
        )
    return f"Program '{program_id}' not found. Available programs: {', '.join(programs.keys())}"


@tool
def check_public_seat_availability(program_id: Optional[str] = None) -> str:
    """Check public seat availability for programs. If no program specified, returns all."""
    seat_data = {
        "civil": {"total": 60, "available": 15},
        "computer": {"total": 65, "available": 8},
        "electrical": {"total": 50, "available": 5},
        "electronics": {"total": 58, "available": 12},
        "architecture": {"total": 55, "available": 20},
    }

    if program_id:
        program_id = program_id.lower()
        data = seat_data.get(program_id)
        if data:
            return (
                f"**{program_id.title()} Engineering**\n"
                f"Total Seats: {data['total']}\n"
                f"Available: {data['available']}\n"
                f"Filled: {data['total'] - data['available']}"
            )
        return f"Program not found."
    else:
        # Return all programs
        result = "**Current Seat Availability (2026)**\n\n"
        for prog, data in seat_data.items():
            result += f"• {prog.title()}: {data['available']}/{data['total']} available\n"
        return result


@tool
def get_admission_information() -> str:
    """Get comprehensive admission process information."""
    return """**KEC Admission Process**

1. **Eligibility Check**
   - Passed +2 / Equivalent qualification
   - IOE entrance exam requirement for some programs

2. **Online Application**
   - Fill application form at KEC portal
   - Upload required documents
   - Application fee payment

3. **Entrance Examination** (For competitive programs)
   - Common entrance exam administered by IOE
   - Results declared within 30 days

4. **Merit-Based Selection**
   - Ranking based on entrance exam + board marks
   - Category-wise seat allocation

5. **Document Verification**
   - Original documents submission
   - Health check-up

6. **Final Registration**
   - Fee payment
   - Orientation program
   - Course enrollment

**Required Documents:**
- School leaving certificate
- Mark sheet copies
- Birth certificate
- Citizenship/Passport
- Entrance exam admit card

Contact: admissions@kec.edu.np | Phone: +977-1-XXXX-XXXX"""


@tool
def get_contact_information() -> str:
    """Get KEC contact details and campus information."""
    return """**Kathmandu Engineering College (KEC)**

📍 **Address:** Lalitpur, Kathmandu, Nepal

📞 **Phone:** +977-1-XXXX-XXXX (Main)
           +977-1-XXXX-XXXX (Admissions)

📧 **Email:** admissions@kec.edu.np
            info@kec.edu.np
            support@kec.edu.np

🕐 **Office Hours:** Monday-Friday, 9:00 AM - 5:00 PM
                   Saturday, 10:00 AM - 2:00 PM
                   Sunday - Closed

🌐 **Website:** www.kecktm.edu.np

**Campus Facilities:**
- Modern classrooms and labs
- Library with digital resources
- Sports complex
- Hostel accommodation
- Cafeteria and recreational areas
- WiFi coverage throughout campus"""


@tool
def get_latest_notices() -> str:
    """Get latest notices and announcements from KEC."""
    return """**Latest KEC Notices & Announcements**

1. **Admission 2026 Open** (August 30, 2026)
   - Apply now for all engineering programs
   - Deadline: September 30, 2026

2. **Entrance Exam Schedule** (August 28, 2026)
   - Date: September 15, 2026
   - Admit cards available online

3. **Semester II Results** (August 25, 2026)
   - Results published on student portal
   - Recheck request deadline: September 5

4. **Campus Reopening** (August 22, 2026)
   - Fall semester starts September 1
   - Student orientation: August 31

For more notices, visit the KEC portal or contact administration."""


@tool
def authenticate_student(student_id: str) -> Dict[str, Any]:
    """Verify student identity for authenticated services.

    Note: Full authentication should happen through secure API endpoints.
    This is a placeholder for the agent to recognize authentication requirements.
    """
    return {
        "authenticated": False,
        "message": "Authentication required. Please log in through the student portal.",
        "requires_login": True,
    }


@tool
def check_student_results(registration_number: str) -> str:
    """Check student academic results (requires authentication)."""
    # TODO: Call backend API with authentication
    return f"Results for student {registration_number}"


@tool
def book_appointment(faculty_id: str, title: str, time: str) -> str:
    """Book an appointment with faculty."""
    # TODO: Call backend API
    return f"Appointment booked with {faculty_id}"


@tool
def reserve_seat(program_id: str, user_confirmation: bool) -> str:
    """Reserve a seat in a program."""
    if not user_confirmation:
        return "User confirmation required"
    # TODO: Call backend API
    return f"Seat reserved for {program_id}"


@tool
def register_program(program_id: str, user_confirmation: bool) -> str:
    """Register for a program."""
    if not user_confirmation:
        return "User confirmation required"
    # TODO: Call backend API
    return f"Registration started for {program_id}"


tools = [
    search_kec_information,
    get_program_information,
    check_public_seat_availability,
    get_admission_information,
    get_contact_information,
    get_notice,
    authenticate_student,
    check_student_results,
    book_appointment,
    reserve_seat,
    register_program,
]


# ============ COLLEXA Agent ============

class Collexa:
    """COLLEXA - Intelligent College Assistant Agent."""

    def __init__(self):
        """Initialize the agent."""
        self.model = ChatGoogleGenerativeAI(
            model="gemini-pro",
            api_key=settings.google_api_key,
            temperature=0.7,
        )
        self.tool_executor = ToolExecutor(tools)

        # Build graph
        self.graph = self._build_graph()

    def _build_graph(self):
        """Build LangGraph workflow."""
        workflow = StateGraph(AgentState)

        # Add nodes
        workflow.add_node("intent_classifier", self._classify_intent)
        workflow.add_node("router", self._route_intent)
        workflow.add_node("respond", self._generate_response)
        workflow.add_node("tool_executor", self._execute_tools)
        workflow.add_node("auth_gate", self._check_authentication)

        # Add edges
        workflow.add_edge("intent_classifier", "router")
        workflow.add_conditional_edges(
            "router",
            self._route_decision,
            {
                "auth_required": "auth_gate",
                "tools_needed": "tool_executor",
                "respond": "respond",
            },
        )
        workflow.add_edge("auth_gate", "tool_executor")
        workflow.add_edge("tool_executor", "respond")
        workflow.add_edge("respond", END)

        return workflow.compile()

    def _classify_intent(self, state: AgentState) -> Dict[str, Any]:
        """Classify user intent from last message."""
        last_message = state.messages[-1]
        query = last_message.content.lower()

        # Simple intent classification
        if any(word in query for word in ["result", "grade", "marks", "gpa"]):
            intent = IntentType.RESULTS
        elif any(word in query for word in ["program", "course", "specialization"]):
            intent = IntentType.PROGRAMS
        elif any(word in query for word in ["admission", "apply", "entrance"]):
            intent = IntentType.ADMISSIONS
        elif any(word in query for word in ["appointment", "faculty", "teacher"]):
            intent = IntentType.APPOINTMENTS
        elif any(word in query for word in ["seat", "vacancy", "available"]):
            intent = IntentType.SEATS
        elif any(word in query for word in ["register", "registration"]):
            intent = IntentType.REGISTRATION
        else:
            intent = IntentType.GENERAL_INFO

        state.messages.append(
            AIMessage(content=f"[INTENT: {intent.value}]", name="intent_classifier")
        )
        return state

    def _route_intent(self, state: AgentState) -> Dict[str, Any]:
        """Route based on classified intent."""
        # Extract intent from messages
        last_message = state.messages[-1]
        if "[INTENT:" in last_message.content:
            return state

        return state

    def _route_decision(self, state: AgentState) -> str:
        """Decide routing direction."""
        last_message = state.messages[-1]
        content = last_message.content

        if "RESULTS" in content or "REGISTRATION" in content:
            return "auth_required"
        elif any(keyword in content for keyword in ["PROGRAMS", "ADMISSIONS", "SEATS"]):
            return "tools_needed"
        else:
            return "respond"

    def _check_authentication(self, state: AgentState) -> Dict[str, Any]:
        """Check if user is authenticated."""
        if state.current_user_id:
            state.requires_auth = False
        else:
            state.requires_auth = True
        return state

    def _execute_tools(self, state: AgentState) -> Dict[str, Any]:
        """Execute necessary tools."""
        # This would call the tool executor
        return state

    def _generate_response(self, state: AgentState) -> Dict[str, Any]:
        """Generate final response."""
        # Use LLM to generate response based on context
        response = self.model.invoke(state.messages)
        state.messages.append(response)
        return state

    async def process_query(
        self,
        query: str,
        session_id: str,
        user_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Process a user query."""
        # Create initial state
        state = AgentState(
            messages=[HumanMessage(content=query)],
            current_user_id=user_id,
            session_id=session_id,
        )

        # Run graph
        result = self.graph.invoke(state)

        # Extract response
        response_msg = result.messages[-1]
        return {
            "response": response_msg.content,
            "requires_auth": result.requires_auth,
            "session_id": session_id,
            "sources": ["knowledge_base"],
            "next_action": None,
        }


# Global agent instance
_collexa_agent: Optional[Collexa] = None


def get_collexa_agent() -> Collexa:
    """Get or create COLLEXA agent instance."""
    global _collexa_agent
    if _collexa_agent is None:
        _collexa_agent = Collexa()
    return _collexa_agent
