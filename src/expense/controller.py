from src.expense.dtos import ExpenseSchema, ExpenseAnlayticsSchema,ExpenseReportSchema
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
        end_date:date | None = None,
        page:int = 1,
        limit:int = 10):
    
    
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

    query = query.order_by(ExpenseModel.created_on.desc())

    offset=(page-1)* limit
    all_expenses=query.offset(offset).limit(limit).all()



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


def analytics(db:Session,user:UserModel):
    result = db.query(
    func.sum(ExpenseModel.amount).label("total_spent"),
    func.count(ExpenseModel.id).label("total_expenses"),
    func.max(ExpenseModel.amount).label("highest_spent"),
    func.min(ExpenseModel.amount).label("lowest_spent"),
    func.avg(ExpenseModel.amount).label("average_spent")).filter(ExpenseModel.user_id == user.id).first()
    
    
    return ExpenseAnlayticsSchema(
    total_expenses=result.total_expenses,
    total_spent=result.total_spent,
    highest_spent=result.highest_spent,
    lowest_spent=result.lowest_spent,
    average_spent=result.average_spent
)

def report(db:Session,user:UserModel):

    report=db.query(ExpenseModel.category,
                    func.sum(ExpenseModel.amount).label("total_spent")
                    ).filter(ExpenseModel.user_id==user.id
                    ).group_by(ExpenseModel.category).all()
    

    result=[]
    for item in report:
        result.append(ExpenseReportSchema(
    category=item.category,
    total_spent=item.total_spent
))
    


    return result