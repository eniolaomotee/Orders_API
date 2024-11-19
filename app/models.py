from .database import Base
from sqlalchemy import Column,String,Integer,Boolean,Float
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationships


class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer,primary_key=True,nullable=False)
    order_name = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    published = Column(Boolean, nullable=False, server_default='False')
    quantity = Column(Integer,nullable=False)
    order_date = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True, nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
    
    
    
    
# @router.get("/", response_model=List[schemas.OrderOut])
# def get_all_orders(db:Session = Depends(get_db)):
#     orders = db.query(models.Order).all()
    
#     return orders
    

# @router.post("/")
# def create_order(order:schemas.OrderCreate, db:Session = Depends(get_db)):
#     new_order = models.Order(**order.dict())
    
#     db.add(new_order)
#     db.commit()
#     db.refresh(new_order)
    
#     return new_order
    
    
# router = APIRouter(
#     prefix="/orders",
#     tags=["Orders"]
# )
