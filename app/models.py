from .database import Base
from sqlalchemy import Column,String,Integer,Boolean,Float,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer,primary_key=True,nullable=False)
    order_name = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    published = Column(Boolean, nullable=False, server_default='False')
    quantity = Column(Integer,nullable=False)
    order_date = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False) # We created a FK so as to match the owner_id to the users id
    
    owner = relationship("User") #Here we created a relationship between the orders and the user, so that we can output which user has which order.
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True, nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
class FoodLike(Base):
    __tablename__ = "foodlikes"
    
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    order_id = Column(Integer,ForeignKey("orders.id",ondelete="CASCADE"),primary_key=True)
    

    
    # pip install pydantic[email]