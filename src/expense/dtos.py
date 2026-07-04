from pydantic import BaseModel
from datetime import datetime
from src.expense.enum import CategoryEnum

class ExpenseSchema(BaseModel):
    amount:float
    category:CategoryEnum
    description:str | None=None
    

class ExpenseResponseSchema(BaseModel):
    id:int
    category:str
    amount:float
    description:str | None=None
    created_on:datetime
    user_id:int 


