from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    order_name: str
    published: bool = True
    price: float
    quantity: int
    
class OrderOut(OrderBase):
    order_name: str
    quantity: str
    published: bool = True
    price: float
    quantity: int

class OrderCreate(OrderBase):
    pass