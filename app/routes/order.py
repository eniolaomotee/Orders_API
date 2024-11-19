from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# get all orders, create_order, get single order, delete order, update order
@router.get("/", response_model=List[schemas.OrderOut])
def get_all_orders(db:Session = Depends(get_db)):
    all_orders = db.query(models.Order).all()
    
    return all_orders

