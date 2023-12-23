from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel,Field

class User(SQLModel,table=True):
    id:int = Field(default=None, primary_key=True)
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@devhub.in.th",
                "password" : "strong!!",
            }
        }

class UserSignIn(SQLModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra ={ 
            "example":{
                "email": "fastapi@devhub.in.th",
                "password": "strong!!",
            }
        }

# class UserList(BaseModel):
#     users : Dict[User.email[User]]

