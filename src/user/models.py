from src.utils.db import Base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__="users"
    
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)
    username=Column(String,unique=True,nullable=False)
    email=Column(String,unique=True,nullable=False)
    hash_password=Column(String, nullable=False)

    expenses=relationship("ExpenseModel",back_populates="user")

    budgets=relationship("BudgetModel",back_populates="user")

