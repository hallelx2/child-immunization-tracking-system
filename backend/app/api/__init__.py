from fastapi import APIRouter
from app.api.v1.endpoints import auth, child_profiles, immunizations, notifications, schedules, milestones, reports
from app.core.config import settings

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(child_profiles.router, prefix="/child_profiles", tags=["Child Profiles"])
api_router.include_router(immunizations.router, prefix="/immunizations", tags=["Immunizations"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
api_router.include_router(schedules.router, prefix="/schedules", tags=["Schedules"])
api_router.include_router(milestones.router, prefix="/milestones", tags=["Milestones"])
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"])
