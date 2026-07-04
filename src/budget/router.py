from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.utils.db import get_db
from src.utils.helpers import is_authenticated

from src.budget import controller
from src.budget.dtos import BudgetSchema, BudgetResponseSchema

budget_routes = APIRouter(
    prefix="/budget"
)


@budget_routes.post(
    "/create",
    response_model=BudgetResponseSchema,
    status_code=status.HTTP_201_CREATED
)
def create_budget(
    body: BudgetSchema,
    db: Session = Depends(get_db),
    user=Depends(is_authenticated)
):
    return controller.create_budget(
        body,
        db,
        user
    )


@budget_routes.get(
    "/idBudget/{budget_id}",
    response_model=BudgetResponseSchema,
    status_code=status.HTTP_200_OK
)
def get_budget_id(
    budget_id: int,
    db: Session = Depends(get_db),
    user=Depends(is_authenticated)
):
    return controller.get_one_budget(
        budget_id,
        db,
        user
    )


@budget_routes.get(
    "/budgets",
    response_model=list[BudgetResponseSchema],
    status_code=status.HTTP_200_OK
)
def get_all_budgets(
    db: Session = Depends(get_db),
    user=Depends(is_authenticated)
):
    return controller.get_all_budgets(
        db,
        user
    )


@budget_routes.put(
    "/update/{budget_id}",
    response_model=BudgetResponseSchema,
    status_code=status.HTTP_200_OK
)
def update_budget(
    body: BudgetSchema,
    budget_id: int,
    db: Session = Depends(get_db),
    user=Depends(is_authenticated)
):
    return controller.update_budget(
        body,
        budget_id,
        db,
        user
    )


@budget_routes.delete(
    "/delete/{budget_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_budget(
    budget_id: int,
    db: Session = Depends(get_db),
    user=Depends(is_authenticated)
):
    return controller.delete_budget(
        budget_id,
        db,
        user
    )