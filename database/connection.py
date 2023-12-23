from sqlmodel import SQLModel, Session, create_engine
from pydantic import BaseSettings
from typing import Optional

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connection_args = {"check_same_thread": False}

engine_url = create_engine(database_connection_string,echo=True,connect_args=connection_args) ## echo is optional for Dev and Prod

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session

class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = None
    ALGORITHM:Optional[str] = None

    class Config:
        env_file = ".env"