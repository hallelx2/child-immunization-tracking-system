from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from app.services.notification_service import NotificationService

router = APIRouter()

class NotificationRequest(BaseModel):
    email: EmailStr
    subject: str
    body: str

@router.post("/")
async def send_notification(request: NotificationRequest, service: NotificationService = Depends()):
    await service.send_notification(request.email, request.subject, request.body)
    return {"msg": "Notification sent successfully"}
