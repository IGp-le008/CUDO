"""COLLEXA Agent - Intelligent multi-step agent with tool calling."""

from typing import Any, Dict, List, Optional, Annotated
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor, ToolInvocation
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from enum import Enum
import json

from config import get_settings

settings = get_settings()


# ============ Agent State ============

class AgentState(BaseModel):
    """State managed by the agent."""
    messages: List[BaseMessage]
    current_user_id: Optional[str] = None
    requires_auth: bool = False
    session_id: str = ""


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


# ============ Tool Definitions ============

@tool
def search_kec_information(query: str) -> str:
    """Search KEC knowledge base for general information."""
    # TODO: Integrate with RAG system
    return f"Information about: {query}"


@tool
def get_program_information(program_id: str) -> str:
    """Get detailed information about a specific program."""
    programs = {
        "civil": "Bachelor of Civil Engineering - 4 years, 60 seats",
        "mechanical": "Bachelor of Mechanical Engineering - 4 years, 60 seats",
        "electrical": "Bachelor of Electrical Engineering - 4 years, 50 seats",
    }
    return programs.get(program_id, "Program not found")


@tool
def check_public_seat_availability(program_id: str) -> str:
    """Check public seat availability for a program."""
    # TODO: Call backend API
    return f"Available seats for {program_id}: 10"


@tool
def get_admission_information() -> str:
    """Get admission process information."""
    return """
    KEC Admission Process:
    1. Fill online application form
    2. Take entrance exam
    3. Merit-based selection
    4. Document verification
    5. Final registration
    """


@tool
def get_contact_information() -> str:
    """Get college contact details."""
    return "KEC, Kathmandu | Phone: +977-1-XXXX-XXXX | Email: admissions@kec.edu.np"


@tool
def get_notice() -> str:
    """Get latest notices from college."""
    # TODO: Call backend API
    return "Latest notices will be fetched from the database"


@tool
def authenticate_student(registration_number: str, password: str) -> bool:
    """Authenticate a student for accessing protected information."""
    # TODO: Call backend API
    return True


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
