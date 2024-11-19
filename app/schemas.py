from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional



class OrderBase(BaseModel):
    order_name: str
    published: bool = True
    price: float
    quantity: int
    
class OrderOut(OrderBase):
    id: int
    order_name: str
    quantity: str
    published: bool = True
    price: float
    quantity: int

class Order(OrderBase):
    id: int
    order_name: str
    order_date: datetime
    published: bool = True
    price: float
    quantity: int
    

class OrderCreate(OrderBase):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True