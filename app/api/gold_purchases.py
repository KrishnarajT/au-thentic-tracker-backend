from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.gold_purchase import GoldPurchase
from app.schemas.gold_purchase import GoldPurchaseCreate, GoldPurchaseUpdate
from app.crud.gold_purchase import get_all, create, update, delete
from app.db.database import get_db

router = APIRouter()

@router.get("/gold-purchases", response_model=list[GoldPurchase])
async def get_all_purchases(user_id: str, db: Session = Depends(get_db)):
    purchases = get_all(db, user_id)
    if not purchases:
        raise HTTPException(status_code=404, detail="No purchases found")
    return purchases

@router.post("/gold-purchases", response_model=GoldPurchase)
async def create_purchase(purchase: GoldPurchaseCreate, db: Session = Depends(get_db)):
    return create(db, purchase)

@router.put("/gold-purchases/{purchase_id}", response_model=GoldPurchase)
async def update_purchase(purchase_id: str, purchase: GoldPurchaseUpdate, db: Session = Depends(get_db)):
    updated_purchase = update(db, purchase_id, purchase)
    if not updated_purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return updated_purchase

@router.delete("/gold-purchases/{purchase_id}", response_model=dict)
async def delete_purchase(purchase_id: str, db: Session = Depends(get_db)):
    success = delete(db, purchase_id)
    if not success:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return {"detail": "Purchase deleted successfully"}