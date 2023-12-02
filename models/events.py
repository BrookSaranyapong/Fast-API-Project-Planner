from sqlmodel import JSON,SQLModel,Field, Column
from typing import List


class Event(SQLModel,table=True):
    id:int = Field(default=None,primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allow = True
        schema_extra = { 
            "example" : {
                "title":"FastAPI Events list" ,
                "image" : "https://my-image.com/img.png",
                "description": "Welcome to event project",
                "tags": ["FastAPI","Python","Devforcat"],
                "location":"Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = { 
            "example" : {
                "title":"FastAPI Events list" ,
                "image" : "https://my-image.com/img.png",
                "description": "Welcome to event project",
                "tags": ["FastAPI","Python","Devforcat"],
                "location":"Google Meet"
            }
        }