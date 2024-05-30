from app.db.models.child_profile import ChildProfile

class ChildProfileRepository:
    def __init__(self, database):
        self.database = database

    async def create_child_profile(self, profile: ChildProfile):
        await self.database["child_profiles"].insert_one(profile.dict())

    async def get_child_profile_by_id(self, profile_id: str):
        return await self.database["child_profiles"].find_one({"id": profile_id})

    async def get_child_profiles_by_user_id(self, user_id: str):
        return await self.database["child_profiles"].find({"user_id": user_id}).to_list(length=100)
