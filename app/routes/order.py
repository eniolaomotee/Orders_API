from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional
from .. import models,schemas,oauth
from sqlalchemy import func
router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# get all orders, create_order, get single order, delete order, update order
@router.get("/",response_model=List[schemas.OrdersOut])
def get_all_orders(db:Session = Depends(get_db), current_user=Depends(oauth.get_current_user), limit:int = 100, skip: int = 0, search: Optional[str] = ""):
    all_orders = db.query(models.Order).filter(models.Order.order_name.contains(search)).limit(limit).offset(skip).all()

    # How to hjoin in sqlalchemy
    results = db.query(models.Order, func.count(models.FoodLike.order_id).label("likes")).join(models.FoodLike,models.FoodLike.order_id == models.Order.id, isouter=True).group_by(models.Order.id).limit(limit).offset(skip).all()
    
    print(results)
     
    return results

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db:Session = Depends(get_db), current_user:int = Depends(oauth.get_current_user)):
            
    new_order = models.Order(owner_id=current_user.id,**order.dict())
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    return new_order

@router.get("/{id}",response_model=schemas.OrderOut)
def get_single_order(id:int, db:Session=Depends(get_db), current_user = Depends(oauth.get_current_user)):
    
    get_order = db.query(models.Order).filter(models.Order.id == id)
    
    new_order = get_order.first()
    
    if new_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with id:{id} not found")
    
    return new_order

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(id: int, db:Session=Depends(get_db),current_user = Depends(oauth.get_current_user)):
    order_query = db.query(models.Order).filter(models.Order.id == id)
    
    del_order = order_query.first()
    
    
    if del_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with id:{id} not found")
    
    if del_order.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not authorized to delete this order please.")
    
    order_query.delete(synchronize_session=False)
    
    db.commit()
    
    return {"message":"Order has been deleted Successfully"}


@router.put("/status/{id}",response_model=schemas.OrderOut)
def update_order_status(id:int,order_update:schemas.OrderStatus, db:Session=Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == id)
    
    order_status = order.first()
    
    if not order_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order not found")
    
    
    order.update({"published":order_update.published},synchronize_session=False)
    
    db.commit()
    
    return order.first()




@router.put("/{id}",response_model=schemas.OrderOut)
def update_order(id:int,order:schemas.OrderCreate,db:Session=Depends(get_db), current_user= Depends(oauth.get_current_user)):
    
    order_query = db.query(models.Order).filter(models.Order.id == id)
    
    updated_order = order_query.first()
    
    
    print(updated_order)
    
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with id:{id} not found")
    
    if updated_order.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not authorized to update this order.")
    
    
    order_query.update(order.dict(),synchronize_session=False)
    
    db.commit()
    
    return order_query.first()