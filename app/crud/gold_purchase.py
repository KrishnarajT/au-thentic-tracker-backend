from sqlalchemy.orm import Session
from app.models.gold_purchase import GoldPurchase
from app.schemas.gold_purchase import GoldPurchaseCreate, GoldPurchaseUpdate

def get_all(db: Session, user_id: int):
    return db.query(GoldPurchase).filter(GoldPurchase.user_id == user_id).all()

def create(db: Session, purchase: GoldPurchaseCreate, user_id: int):
    db_purchase = GoldPurchase(**purchase.dict(), user_id=user_id)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def update(db: Session, purchase_id: int, purchase: GoldPurchaseUpdate):
    db_purchase = db.query(GoldPurchase).filter(GoldPurchase.id == purchase_id).first()
    if db_purchase:
        for key, value in purchase.dict(exclude_unset=True).items():
            setattr(db_purchase, key, value)
        db.commit()
        db.refresh(db_purchase)
    return db_purchase

def delete(db: Session, purchase_id: int):
    db_purchase = db.query(GoldPurchase).filter(GoldPurchase.id == purchase_id).first()
    if db_purchase:
        db.delete(db_purchase)
        db.commit()
    return db_purchase is not None