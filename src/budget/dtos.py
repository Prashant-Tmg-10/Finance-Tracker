
from pydantic import BaseModel
from datetime import datetime
from src.budget.enum import Period

class BudgetSchema(BaseModel):
    amount: float
    period: Period



class BudgetResponseSchema(BaseModel):
    id: int
    amount: float
    period: Period
    start_date: datetime
    end_date: datetime
    created_on: datetime
    user_id: int