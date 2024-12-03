from pydantic import BaseModel,EmailStr,Field
from datetime import datetime
from typing import Optional



class OrderBase(BaseModel):
    order_name: str
    published: bool = True
    price: float
    quantity: int
    
class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True


class OrderOut(OrderBase):
    id:int
    owner_id:int
    owner: UserOut
    
    class Config:
        from_attributes = True 


class OrdersOut(BaseModel):
    Order: OrderOut
    likes: int
    
    
class OrderCreate(OrderBase):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    

        
class OrderStatus(BaseModel):
    published: bool
    

class Token(BaseModel):
    access_token: str
    token_type:str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    

class FoodLike(BaseModel):
    order_id : int
    dir: int = Field(..., ge=0, le=1)


class Order(OrderBase):
    id: int
    order_name: str
    order_date: datetime
    published: bool = True
    price: float
    quantity: int
    
    
    
    
    





