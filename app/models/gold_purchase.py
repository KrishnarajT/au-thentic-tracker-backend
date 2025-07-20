from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class GoldPurchase(Base):
    __tablename__ = 'gold_purchases'

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="gold_purchases")