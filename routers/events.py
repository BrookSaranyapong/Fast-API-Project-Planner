from fastapi import APIRouter, HTTPException, status, Body, Depends
from models.events import Event, EventUpdate
from typing import List
from auth.authenticate import authenticate

from sqlmodel import select, delete
from database.connection import get_session

event_router = APIRouter(tags=["Events"],dependencies=[Depends(authenticate)]) #Midleware Router Level 

events = []

@event_router.get("/",response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)):
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}",response_model=Event)
async def retrieve_event(id: int,session=Depends(get_session)) -> Event:
    event = session.get(Event,id)
    if event: 
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event ID not exist!"
    )

@event_router.post("/new",status_code=status.HTTP_201_CREATED)
async def create_event(new_event: Event,session=Depends(get_session)):
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    
    return {"message" : "Event Created Successfully"}

@event_router.put("/edit/{id}",response_model=Event)
async def update_event(id: int, new_data:EventUpdate,session=Depends(get_session)):
    event = session.get(Event,id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key,value in event_data.items():
            setattr(event,key,value)
        
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with ID not exist!"
    )

@event_router.delete("/{id}")
async def delete_event(id:int,session=Depends(get_session)):
    event = session.get(Event,id)
    if event:
        session.delete(event)
        session.commit()
        return {
            "message" : "Event Delete successfully"
        }
    raise HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event Id does not exist!"
    )

@event_router.delete("/")
async def delete_all_events(session=Depends(get_session)):
    statement = delete(Event)
    session.execute(statement)
    session.commit()

    result = session.execute(select(Event))
    all_row = result.fetchall()
    if len(all_row) == 0 : 
        return {
            "message": "Event deleted successfully"
        }
    raise HTTPException (
        status_code=status.HTTP_409_CONFLICT,
        detail="Event Delete not successfully"
    )