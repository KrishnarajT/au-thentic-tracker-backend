from fastapi import APIRouter, HTTPException
from app.schemas.settings import Settings, SettingsUpdate
from app.crud.settings import get_settings, update_settings

router = APIRouter()

@router.get("/settings", response_model=Settings)
async def get_user_settings():
    settings = await get_settings()
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings

@router.put("/settings", response_model=Settings)
async def update_user_settings(settings_update: SettingsUpdate):
    updated_settings = await update_settings(settings_update)
    if not updated_settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return updated_settings