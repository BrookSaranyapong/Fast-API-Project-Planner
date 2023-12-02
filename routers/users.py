from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=["user"])

users = {}

@user_router.post("/signup",status_code=201)
async def sign_new_user(data:User):
    if data.email in users:
        raise HTTPException (
            status_code=status.HTTP_409_CONFLICT,
            detail="Email exists"
        )
    users[data.email] = data

    return {
        "message": "User register successfully"
    }

@user_router.post("/signin")
async def sign_user_in(user:UserSignIn):
    if not users.get(user.email):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist!"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential"
        )
    
    return {
        "message" : "User signed in successfully"
    }

@user_router.get("/users")
async def retrieve_all_user():
    return {"users": users}