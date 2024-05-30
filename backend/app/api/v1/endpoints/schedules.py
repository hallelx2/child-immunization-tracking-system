from fastapi import APIRouter, Depends, HTTPException
from app.db.repositories.schedule import ScheduleRepository
from app.db.models.schedule import Schedule

router = APIRouter()

@router.post("/")
async def create_schedule(schedule: Schedule, repo: ScheduleRepository = Depends()):
    await repo.create_schedule(schedule)
    return {"msg": "Schedule created successfully"}

@router.get("/{child_id}")
async def get_schedules(child_id: str, repo: ScheduleRepository = Depends()):
    schedules = await repo.get_schedules_by_child_id(child_id)
    if not schedules:
        raise HTTPException(status_code=404, detail="No schedules found for the child")
    return schedules
