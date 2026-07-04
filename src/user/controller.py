from src.user.dtos import UserSchema,loginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException,status,Request
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime,timedelta
import jwt
from jwt.exceptions import InvalidTokenError

password_hash=PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)



#Registraion
def register(body:UserSchema,db:Session):
    is_user=db.query(UserModel).filter(UserModel.username==body.username).first()


    if is_user:
        raise HTTPException(400,detail="Username already exists...")
    
    is_user=db.query(UserModel).filter(UserModel.email==body.email).first()

    if is_user:
        raise HTTPException(400,detail="Email already exists")
    
    
     
    hashed_password=get_password_hash(body.password)

    new_user=UserModel(
        name=body.name,
        username=body.username,
        hash_password=hashed_password,
        email=body.email,

    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return new_user


def login(body:loginSchema,db:Session):
    user=db.query(UserModel).filter(UserModel.username==body.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    
    if not verify_password(body.password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    
    exp_time=datetime.now() + timedelta(minutes=settings.EXP_TIME)
    print(exp_time)

    token=jwt.encode({"_id":user.id,"exp":exp_time.timestamp()},settings.SECRET_KEY,settings.ALGORITHM)
    

    

    return {"token":token}

##Token send
def is_authenticated(request:Request,db:Session):
    try:    
        token=request.headers.get("authorization")
       # print("TOKEN:", token)
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credentials")
        
        token=(token.split(" ")[-1])

        data=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        user_id=data.get("_id")

        user=db.query(UserModel).filter(UserModel.id==user_id).first()
       # print("PAYLOAD:", data)
        #print("USER_ID:", user_id)
        #print("USER:", user)


        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credetianls")
        

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")

