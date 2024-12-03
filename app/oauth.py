from fastapi import HTTPException,status, Depends
from datetime import datetime,timedelta
from . import models,schemas
from .database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .config import settings
from jose import jwt, JWTError


oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM =settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expires_minutes


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return token


def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        
        id: str = str(payload.get("user_id"))
        
        if id is None:
            raise credentials_exception
        user_data= schemas.TokenData(id=id)
        
    except JWTError as e:
        print("JWTError",e)
        raise  credentials_exception
    
    return user_data


def get_current_user(token: str = Depends(oauth_scheme), db:Session = Depends(get_db)):
    
    credentials_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials",
                                          headers={"WWW-Authenticate":"Bearer"})
    
    token_user = verify_token(token,credentials_exception)
    
    user = db.query(models.User).filter(models.User.id == token_user.id).first()
    
    return user






