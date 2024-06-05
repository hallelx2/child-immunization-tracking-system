from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from app.db.repositories.child_profile import ChildProfileRepository
from app.db.models.child_profile import ChildProfile
from app.api.v1.dependency import CurrentUser

router = APIRouter()

@router.post("/")
async def create_child_profile(profile: ChildProfile, repo: ChildProfileRepository = Depends()):
    await repo.create_child_profile(profile)
    return {"msg": "Child profile created successfully"}

@router.get("/{user_id}")
async def get_child_profiles(user_id: str, repo: Annotated[ChildProfileRepository, Depends()], current_user: CurrentUser):
    profiles = await repo.get_child_profiles_by_user_id(user_id)
    if not profiles:
        raise HTTPException(status_code=404, detail="No profiles found for the user")
    return profiles
