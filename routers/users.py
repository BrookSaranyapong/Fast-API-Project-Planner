from fastapi import APIRouter, HTTPException, status,Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.users import User, UserSignIn,TokenResponse

from auth.jwt_handler import create_access_token

from sqlmodel import select
from database.connection import get_session
from auth.hash_password import HashPassword

user_router = APIRouter(tags=["user"])

hash_password = HashPassword()

@user_router.post("/signup",status_code=201)
async def sign_new_user(user:User, session=Depends(get_session)):
    statement = select(User).where(User.email == user.email)
    result = session.exec(statement)
    if result.first():
        raise HTTPException (
            status_code=status.HTTP_409_CONFLICT,
            detail="Email exists"
        )
    else:
        hash_pwd = hash_password.create_hash(user.password)
        user.password = hash_pwd

        session.add(user)
        session.commit()
        session.refresh(user)

        return {
            "message": "User register successfully"
        }

@user_router.post("/signin",response_model=TokenResponse)
async def sign_user_in(user:OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)):
# async def sign_user_in(user:UserSignIn, session=Depends(get_session)): UserSignIn BaseModel Form
    statement = select(User).where(User.email == user.username)
    # statement = select(User).where(User.email == user.email)  UserSignIn BaseModel Form
    result = session.exec(statement)
    user_data = result.first()

    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist!"
        )
    
    if not hash_password.verify_hash(user.password,user_data.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential"
        )
    
    access_token = create_access_token(user_data.email)
    # TokenResponse.access_token = access_token
    # TokenResponse.token_type = "Bearer"
    # return TokenResponse
    return {
        "access_token":access_token,
        "token_type": "Bearer",
        "message" : "User signed in successfully"
    }


"""
@user_router.get("/users")
async def retrieve_all_user():
    return {"users": users}
"""
