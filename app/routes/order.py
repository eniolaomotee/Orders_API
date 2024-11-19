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

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db:Session = Depends(get_db)):
    new_order = models.Order(**order.dict())
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    return new_order

@router.get("/{id}")
def get_single_order(id:int, db:Session=Depends(get_db)):
    
    get_order = db.query(models.Order).filter(models.Order.id == id)
    
    new_order = get_order.first()
    
    if new_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with id:{id} not found")
    
    return new_order

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(id: int, db:Session=Depends(get_db)):
    order_query = db.query(models.Order).filter(models.Order.id == id)
    
    del_order = order_query.first()
    
    
    if del_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with id:{id} not found")
    
    order_query.delete(synchronize_session=False)
    
    db.commit()
    
    return {"message":"Order has been deleted Successfully"}


@router.put("/{id}")
def update_order(id:int,order:schemas.OrderCreate,db:Session=Depends(get_db)):
    
    order_query = db.query(models.Order).filter(models.Order.id == id)
    
    updated_order = order_query.first()
    
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with id:{id} not found")
    
    
    order_query.update(order.dict(),synchronize_session=False)
    
    db.commit()
    
    return order_query.first()