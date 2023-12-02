from pydantic import BaseModel, EmailStr
from typing import List,Optional,Dict
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@devhub.in.th",
                "password" : "strong!!",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra ={ 
            "example":{
                "email": "fastapi@devhub.in.th",
                "password": "strong!!",
            }
        }

# class UserList(BaseModel):
#     users : Dict[User.email[User]]

