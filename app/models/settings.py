from sqlalchemy import Column, String, Boolean
from app.db.database import Base

class Settings(Base):
    __tablename__ = 'settings'

    id = Column(String, primary_key=True, index=True)
    currency = Column(String, index=True)
    auto_fetch_price = Column(Boolean, default=True)