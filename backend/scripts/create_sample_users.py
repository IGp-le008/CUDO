"""Create sample users for testing."""

import asyncio
import logging

from database import get_db_session, init_db
from models import User
from auth import hash_password

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_sample_users():
    """Create sample users for testing."""
    logger.info("📝 Creating sample users...")

    # Initialize DB
    await init_db()

    sample_users = [
        {
            "email": "student1@kec.edu.np",
            "full_name": "Ramesh Sharma",
            "registration_number": "KEC001",
            "phone": "+977-98XXXXXXX",
            "password": "TestPassword123",
        },
        {
            "email": "student2@kec.edu.np",
            "full_name": "Priya Poudel",
            "registration_number": "KEC002",
            "phone": "+977-98XXXXXXX",
            "password": "TestPassword123",
        },
        {
            "email": "admin@kec.edu.np",
            "full_name": "Admin User",
            "password": "AdminPassword123",
            "is_admin": True,
        },
    ]

    async with get_db_session() as session:
        for user_data in sample_users:
            try:
                user = User(
                    email=user_data["email"],
                    full_name=user_data["full_name"],
                    registration_number=user_data.get("registration_number"),
                    phone=user_data.get("phone"),
                    password_hash=hash_password(user_data["password"]),
                    is_active=True,
                    is_admin=user_data.get("is_admin", False),
                )
                session.add(user)
                logger.info(f"✅ Created user: {user_data['email']}")
            except Exception as e:
                logger.error(f"❌ Error creating user {user_data['email']}: {e}")

        await session.commit()

    logger.info("✅ Sample users created successfully")


if __name__ == "__main__":
    asyncio.run(create_sample_users())
