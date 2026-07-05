
from pydantic import BaseModel
from datetime import datetime
from src.budget.enum import Period
from datetime import date

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

class BudgetSummaryResponse(BaseModel):
    budget_amount:float
    total_spent:float
    remaining:float
    used_percentage:float
    status:str
    period:str
    start_date:datetime
    end_date:datetime

