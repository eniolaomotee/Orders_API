from fastapi import HTTPException,status
from datetime import datetime,timedelta
from . import models,schemas
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .config import settings
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRES_MINUTES=settings.access_token_expires_minutes



def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    to_encode.update({"exp":expire})
    
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


