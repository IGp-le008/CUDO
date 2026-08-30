"""Sample KEC knowledge base data for RAG system."""

KEC_KNOWLEDGE_BASE = [
    {
        "title": "Kathmandu Engineering College - Overview",
        "content": """Kathmandu Engineering College (KEC) is a premier engineering institution in Nepal,
        established to provide world-class engineering education. Located in Kathmandu, KEC offers
        comprehensive programs in Civil, Mechanical, and Electrical Engineering with state-of-the-art facilities.""",
        "category": "general",
    },
    {
        "title": "Admission Process",
        "content": """KEC Admission Process:
        1. Fill online application form on our website
        2. Eligible candidates take the entrance examination
        3. Merit-based selection from top scorers
        4. Document verification
        5. Final registration and fee payment
        Application deadline: September 30 annually.
        Entrance exam held: October
        Selection results: November""",
        "category": "admissions",
    },
    {
        "title": "Bachelor of Civil Engineering",
        "content": """A 4-year comprehensive program covering structural design, construction management,
        environmental engineering, and infrastructure development. Total 60 seats available.
        Curriculum includes practical labs, field work, and industry internships.""",
        "category": "programs",
    },
    {
        "title": "Bachelor of Mechanical Engineering",
        "content": """A 4-year program focusing on thermodynamics, machine design, manufacturing processes,
        and renewable energy. 60 seats available. Includes workshops on CAD, CNC machining, and automation.""",
        "category": "programs",
    },
    {
        "title": "Bachelor of Electrical Engineering",
        "content": """A 4-year program covering power systems, electrical machines, control systems,
        and renewable energy. 50 seats available. Emphasizes practical skills in electrical design and installation.""",
        "category": "programs",
    },
    {
        "title": "Campus Facilities",
        "content": """KEC provides excellent facilities including:
        - Modern laboratories for all engineering disciplines
        - Well-equipped workshops for practical training
        - Sports facilities and gymnasium
        - Library with digital resources
        - Hostel accommodation for out-station students
        - Cafeteria with healthy food options
        - WiFi coverage across campus""",
        "category": "general",
    },
    {
        "title": "Faculty and Staff",
        "content": """KEC has over 100 highly qualified faculty members with advanced degrees from
        prestigious international universities. Our faculty combines theoretical knowledge with
        practical industry experience.""",
        "category": "general",
    },
    {
        "title": "Tuition Fees",
        "content": """Annual tuition fees for programs:
        - Civil Engineering: NPR 4,50,000
        - Mechanical Engineering: NPR 4,50,000
        - Electrical Engineering: NPR 4,50,000
        Scholarships available for meritorious and financially needy students.
        Installment payment options also available.""",
        "category": "admissions",
    },
    {
        "title": "Contact Information",
        "content": """Kathmandu Engineering College
        Address: Btespur, Kathmandu, Nepal
        Main Phone: +977-1-XXXX-XXXX
        Email: admissions@kec.edu.np
        Office Hours: Monday-Friday, 9 AM - 5 PM
        Emergency Contact: +977-XXXX-XXXX""",
        "category": "general",
    },
]


def get_knowledge_base():
    """Get sample knowledge base."""
    return KEC_KNOWLEDGE_BASE
