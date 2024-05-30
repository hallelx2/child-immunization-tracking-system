from fastapi import FastAPI
from app.api.v1.endpoints import auth, child_profiles, immunizations, notifications, schedules, milestones, reports

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(child_profiles.router, prefix="/api/v1/child_profiles", tags=["Child Profiles"])
app.include_router(immunizations.router, prefix="/api/v1/immunizations", tags=["Immunizations"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["Notifications"])
app.include_router(schedules.router, prefix="/api/v1/schedules", tags=["Schedules"])
app.include_router(milestones.router, prefix="/api/v1/milestones", tags=["Milestones"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
