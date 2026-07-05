from src.budget.models import BudgetModel
from src.expense.models import ExpenseModel
from src.budget.dtos import BudgetSchema
from src.user.models import UserModel
from sqlalchemy.orm import Session 
from fastapi import HTTPException
from datetime import datetime, timedelta,date
from src.budget.enum import Period
from sqlalchemy import func



def create_budget(body, db, user):

    start_date = datetime.utcnow()

    if body.period == Period.DAILY:
        end_date = start_date + timedelta(days=1)

    elif body.period == Period.WEEKLY:
        end_date = start_date + timedelta(days=7)

    elif body.period == Period.MONTHLY:
        end_date = start_date + timedelta(days=30)

    new_budget = BudgetModel(
        amount=body.amount,
        period=body.period,
        start_date=start_date,
        end_date=end_date,
        user_id=user.id
    )

    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)

    return new_budget


def get_one_budget(
    budget_id: int,
    db: Session,
    user: UserModel
):
    budget = (
        db.query(BudgetModel)
        .filter(BudgetModel.id == budget_id)
        .first()
    )

    if not budget:
        raise HTTPException(
            404,
            detail="Budget not found"
        )

    if budget.user_id != user.id:
        raise HTTPException(
            403,
            detail="Access denied"
        )

    return budget


def get_all_budgets(
    db: Session,
    user: UserModel
):
    budgets = (
        db.query(BudgetModel)
        .filter(BudgetModel.user_id == user.id)
        .all()
    )

    return budgets


def update_budget(
    body: BudgetSchema,
    budget_id: int,
    db: Session,
    user: UserModel
):
    budget = (
        db.query(BudgetModel)
        .filter(BudgetModel.id == budget_id)
        .first()
    )

    if not budget:
        raise HTTPException(
            404,
            detail="Budget not found"
        )

    if budget.user_id != user.id:
        raise HTTPException(
            403,
            detail="Access denied"
        )

    data = body.model_dump()

    for field, value in data.items():
        setattr(budget, field, value)

    db.commit()
    db.refresh(budget)

    return budget


def delete_budget(
    budget_id: int,
    db: Session,
    user: UserModel
):
    budget = (
        db.query(BudgetModel)
        .filter(BudgetModel.id == budget_id)
        .first()
    )

    if not budget:
        raise HTTPException(
            404,
            detail="Budget not found"
        )

    if budget.user_id != user.id:
        raise HTTPException(
            403,
            detail="Access denied"
        )

    db.delete(budget)
    db.commit()

    return None


def summary(db:Session,user:UserModel):
    
    today=datetime.now()
       
    budgets = (
        db.query(BudgetModel)
        .filter(
            BudgetModel.user_id == user.id,
            BudgetModel.start_date <= today,
            BudgetModel.end_date >= today
        )
        .first()
    )

    if not budgets:
        raise HTTPException(404,detail="No active budget found")
    
    total_spent=(db.query(func.sum(ExpenseModel.amount))
                         .filter(ExpenseModel.user_id==user.id,
                                 ExpenseModel.created_on>=budgets.start_date,
                                 ExpenseModel.created_on<=budgets.end_date,
                                
                         ).scalar()) or 0
    
    remaining=budgets.amount - total_spent

    used_percentage = round(
    (total_spent / budgets.amount) * 100,
    2
    ) if budgets.amount > 0 else 0

    if used_percentage<50:
        status="SAFE"

    elif used_percentage<80:
        status="Warning"
    
    elif used_percentage<=100:
        status="warning"
    else:
        status="EXCEED"

    return {
    "budget_amount": budgets.amount,
    "total_spent": total_spent,
    "remaining": remaining,
    "used_percentage": used_percentage,
    "status": status,
    "period": budgets.period,
    "start_date": budgets.start_date,
    "end_date": budgets.end_date
}
    