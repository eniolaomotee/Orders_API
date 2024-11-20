from fastapi import APIRouter,Depends,status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_db
from .. import models,utils
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Authentication"]
)



@router.post("/login")
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    
    # # Password check 
    if not utils.verify_password(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    
    
    return {"Testing"}