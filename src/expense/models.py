from src.utils.db import Base
from sqlalchemy import Column,String,Integer,DECIMAL,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class ExpenseModel(Base):
    __tablename__="expense"

    id=Column(Integer, primary_key=True, index= True)
    user_id=Column(Integer, ForeignKey("users.id"))
    amount=Column(DECIMAL, nullable=False)
    category=Column(String, nullable=False)
    description=Column(String)
    created_on=Column(DateTime, default=datetime.utcnow)
    updated_on=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

    user=relationship("UserModel",back_populates="expenses")




