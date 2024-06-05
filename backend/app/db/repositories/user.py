from app.db.models.user import User

class UserRepository:
    def __init__(self, database):
        self.database = database.get_collection("users")
        #self.database = database

    async def create_user(self, user: User):
        await self.database.insert_one(user.model_dump())
        #await self.database["users"].insert_one(user.model_dump())

    async def get_user_by_email(self, email: str):
        return await self.database.find_one({"email": email})
        #return await self.database["users"].find_one({"email": email})

    async def get_user_by_id(self, user_id: str):
        return await self.database.find_one({"id": user_id})
        #return await self.database["users"].find_one({"id": user_id})
