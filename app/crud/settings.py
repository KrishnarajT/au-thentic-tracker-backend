from sqlalchemy.orm import Session
from app.models.settings import Settings
from app.schemas.settings import SettingsCreate, SettingsUpdate

def get(db: Session, user_id: int) -> Settings:
    return db.query(Settings).filter(Settings.user_id == user_id).first()

def update(db: Session, user_id: int, settings_update: SettingsUpdate) -> Settings:
    settings = db.query(Settings).filter(Settings.user_id == user_id).first()
    if settings:
        for key, value in settings_update.dict(exclude_unset=True).items():
            setattr(settings, key, value)
        db.commit()
        db.refresh(settings)
    return settings