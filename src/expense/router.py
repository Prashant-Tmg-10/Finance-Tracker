from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.expense import controller
from src.expense.dtos import ExpenseSchema,ExpenseResponseSchema
from src.utils.helpers import is_authenticated

expense_routes=APIRouter(prefix="/expense")

@expense_routes.post("/create",response_model=ExpenseResponseSchema,status_code=status.HTTP_201_CREATED)
def create_expense(body:ExpenseSchema,db:Session=Depends(get_db),user=Depends(is_authenticated)):
    return controller.create_expense(body,db,user)


@expense_routes.get("/idExpenses/{expense_id}",response_model=ExpenseResponseSchema,status_code=status.HTTP_200_OK)
def get_expense_id(expense_id:int,db:Session=Depends(get_db),user=Depends(is_authenticated)):
    return controller.get_one_expense(expense_id,db,user)


@expense_routes.get("/expenses",response_model=list[ExpenseResponseSchema],status_code=status.HTTP_200_OK)
def get_all_expenses(db:Session=Depends(get_db),user=Depends(is_authenticated)):
    return controller.get_all_expenses(db,user)


@expense_routes.put("/update/{expense_id}",response_model=ExpenseResponseSchema,status_code=status.HTTP_201_CREATED)
def update_expense(body:ExpenseSchema,expense_id:int,db:Session=Depends(get_db),user=Depends(is_authenticated)):
    return controller.update_expense(body,expense_id,db,user)


@expense_routes.delete("/delete/{expense_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id:int,db:Session=Depends(get_db),user=Depends(is_authenticated)):
    return controller.delete_expense(expense_id,db,user)