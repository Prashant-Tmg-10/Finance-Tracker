"""import os

print("FILE LOADED:", os.path.abspath(__file__))"""

from fastapi import FastAPI
from src.utils.db import Base,engine
from src.user.models import UserModel
from src.expense.models import ExpenseModel
from src.user.router import user_routes
from src.expense.router import expense_routes
from src.budget.models import BudgetModel
from src.budget.router import budget_routes



Base.metadata.create_all(bind=engine)
app=FastAPI(title="Expense Tracker Appppppp")
app.include_router(user_routes)
app.include_router(expense_routes)
app.include_router(budget_routes)

"""for route in app.routes:
    print(route.path)

@app.get("/hello-expense")
def hello():
    return {"app": "expense tracker"}"""