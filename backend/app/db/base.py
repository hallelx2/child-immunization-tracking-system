from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from app.db.repositories.user import UserRepository

client = AsyncIOMotorClient(settings.DATABASE_URL)
database = client.get_default_database()

# Collection for the user repository
user_repo = UserRepository(database)