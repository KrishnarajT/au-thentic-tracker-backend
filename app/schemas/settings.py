from pydantic import BaseModel

class Settings(BaseModel):
    currency: str
    auto_fetch_price: bool

class SettingsUpdate(BaseModel):
    currency: str = None
    auto_fetch_price: bool = None