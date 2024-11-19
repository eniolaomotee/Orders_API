from fastapi import APIRouter,HTTPException,status,Depends
from .. import models,schemas
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Users"],
    prefix="/users"
)


@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    new_user =models.User(**user.dict())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int, db:Session=Depends(get_db)):
    
    query = db.query(models.User).filter(models.User.id == id)
    
    delete_user = query.first()
    
    if delete_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id:{id} does not exist")
    
    query.delete(synchronize_session=False)
    
    db.commit()