from fastapi import APIRouter,status,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import oauth,schemas,models
from ..database import get_db


router = APIRouter(
    prefix="/likes",
    tags=["Like A Food Type"]
)

@router.post("/")
def like_order(like: schemas.FoodLike,db:Session= Depends(get_db), current_user= Depends(oauth.get_current_user)):
     # get order
    order = db.query(models.Order).filter(models.Order.id == like.order_id).first()
    
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with id:{like.order_id} not found")

    like_query = db.query(models.FoodLike).filter(models.FoodLike.order_id == like.order_id, models.FoodLike.user_id == current_user.id)
    found_like = like_query.first()
    
    
    if (like.dir == 1):
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Order with id {found_like.order_id} has been Liked by user {found_like.user_id}")
        
        new_like = models.FoodLike(order_id=like.order_id,user_id=current_user.id)
        db.add(new_like)
        db.commit()
        
        return {"message":"Successfully Liked order"}   
    
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Like does not exist for user {current_user.id} on order {like.order_id}")
        
        like_query.delete(synchronize_session=False)
        db.commit()
        
        return {"message":"Like has been deleted successfully"}
    
    
    
    
    
    
    
# db.query(models.Order, func.count(models.FoodLike.order_id).label("orders")).join(models.FoodLike, models.FoodLike.order_id == models.Order.id,isouter=True).group_by(models.Order.id)