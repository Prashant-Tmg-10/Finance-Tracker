from src.utils.db import Base
from sqlalchemy import Column,String,Integer,DECIMAL,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class BudgetModel(Base):
    __tablename__="budgets"


    id=Column(Integer,primary_key=True, index=True)
    amount=Column(DECIMAL, nullable=False)
    period=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey("users.id"))
    start_date=Column(DateTime,nullable=False)
    end_date=Column(DateTime,nullable=False)

    created_on=Column(DateTime, default=datetime.utcnow)
    update_on=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

    user=relationship("UserModel",back_populates="budgets")

