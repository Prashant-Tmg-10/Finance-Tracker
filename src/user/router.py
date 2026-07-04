from fastapi import APIRouter,Depends,status,Request
from sqlalchemy.orm import Session
from src.user.dtos import UserSchema,UserResponse,loginSchema
from src.utils.db import get_db
from src.user import controller

user_routes=APIRouter(prefix="/user1")

@user_routes.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controller.register(body,db)


@user_routes.post("/login",status_code=status.HTTP_200_OK)
def login(body:loginSchema,db:Session=Depends(get_db)):
    return controller.login(body,db)


@user_routes.get("/is_auth",response_model=UserResponse,status_code=status.HTTP_200_OK)
def is_auth(request:Request,db:Session=Depends(get_db)):
    return controller.is_autenticated(request,db)