from src.expense.dtos import ExpenseSchema
from sqlalchemy.orm import Session
from src.expense.models import ExpenseModel
from src.user.models import UserModel
from fastapi import HTTPException
from src.expense.enum import CategoryEnum
from datetime import date
from sqlalchemy import func


def create_expense(body:ExpenseSchema,db:Session,user:UserModel):
    data=(body.model_dump())
    new_expense=ExpenseModel(user_id=user.id,
                             amount=data["amount"],
                             category=data["category"],
                             description=data["description"],
                        

                             )
    
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)



    return new_expense



#Get only one expense by user wants to --raw ,later edit
def get_one_expense(expense_id:int,db:Session,user:UserModel):
    one_expense=db.query(ExpenseModel).filter(ExpenseModel.id==expense_id).first()
    if not one_expense:
        raise HTTPException(404,detail="Expense not found")
    
    if one_expense.user_id !=user.id:
        raise HTTPException(401,detail="Invalid credentials")
    

    return one_expense


#get all expenses by user -- later edit
def get_all_expenses(
        db:Session,
        user:UserModel,
        category:CategoryEnum | None = None,
        min_amount:float | None = None,
        max_amount:float | None= None,
        start_date:date | None = None,
        end_date:date | None = None,):
    
    
    query=db.query(ExpenseModel).filter(ExpenseModel.user_id==user.id)

    
    if category:
        query=query.filter(ExpenseModel.category==category.value)

    if min_amount is not None:
        query=query.filter(ExpenseModel.amount>=min_amount)

    if max_amount is not None:
        query=query.filter(ExpenseModel.amount<=max_amount)

    if start_date is not None:
        query=query.filter(func.date(ExpenseModel.created_on)>=start_date)

    if end_date is not None:
        query=query.filter(func.date(ExpenseModel.created_on)<=end_date)

    all_expenses=query.all()



    return all_expenses



#update expenses by ids --editing ...
def update_expense(body:ExpenseSchema,expense_id:int,db:Session,user:UserModel):
    one_expense:ExpenseModel=db.query(ExpenseModel).filter(ExpenseModel.id==expense_id).first()

    if not one_expense:
        raise HTTPException(404,detail="Expense Not found")
    
    if one_expense.user_id != user.id:
        raise HTTPException(403,detail="You cannot update this expense")
    
    body=body.model_dump()
    for field,value in body.items():
        setattr(one_expense,field,value)

    
    db.add(one_expense)
    db.commit()
    db.refresh(one_expense)


    return one_expense

def delete_expense(expense_id:int,db:Session,user:UserModel):
    one_expense=db.query(ExpenseModel).filter(ExpenseModel.id==expense_id).first()
    if not one_expense:
        raise HTTPException(404,detail="Expense not found")
    
    if one_expense.user_id !=user.id:
        raise HTTPException(401,detail="Invalid Expenses")
    
    db.delete(one_expense)
    db.commit()


    return None