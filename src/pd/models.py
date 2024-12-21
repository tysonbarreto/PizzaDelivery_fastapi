from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(100),unique=True)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)
    orders=relationship("Order",back_populates="user")

    def __repr__(self):
        return f"<User {self.username}"
    

class Order(Base):

    ORDER_STATUS = (
        ("PENDING","pending"),
        ("IN-TRANSIT","in-transit"),
        ("DELIVERED","delivered"),
    )

    SIZES=(
        ("SMALL","small"),
        ("MEDIUM","medium"),
        ("LARGE","large"),
        ("XLARGE","xlarge")
    )
    __tablename__="orders"
    id=Column(Integer,primary_key=True)
    quantity=Column(Integer,nullable=True)
    order_status=Column(ChoiceType(choices=ORDER_STATUS), default="PENDING")
    sizes=Column(ChoiceType(choices=SIZES), default="MEDIUM")
    user_id=Column(Integer,ForeignKey("user.id"))
    user=relationship("User",back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}"


if __name__=="__main__":
    __all__ = ["User","Order"]

