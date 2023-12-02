from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id:int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = { 
            "example" : {
                "id" : 1,
                "title":"FastAPI Events list" ,
                "image" : "https://my-image.com/img.png",
                "description": "Welcome to event project",
                "tags": ["FastAPI","Python","Devforcat"],
                "location":"Google Meet"
            }
        }