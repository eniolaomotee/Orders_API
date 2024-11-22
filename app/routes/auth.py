from fastapi import APIRouter,Depends,status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_db
from .. import models,utils, oauth
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Authentication"]
)



@router.post("/login")
def login_user(user_credentials: OAuth2PasswordRequestForm= Depends(),db:Session = Depends(get_db)):
    user_to_log = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user_to_log or not utils.verify_password(user_credentials.password,user_to_log.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    
    
    access_token = oauth.create_access_token(data={"user_id": user_to_log.id})
    
    return {"access_token": access_token,"token-type":"Bearer"}
    
    return {"Testing"}