from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GoldPurchaseBase(BaseModel):
    user_id: str
    amount: float
    date: datetime

class GoldPurchaseCreate(GoldPurchaseBase):
    pass

class GoldPurchaseUpdate(BaseModel):
    amount: Optional[float] = None
    date: Optional[datetime] = None

class GoldPurchase(GoldPurchaseBase):
    id: int

    class Config:
        orm_mode = True