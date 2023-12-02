from fastapi import APIRouter, HTTPException, status, Body
from models.events import Event
from typing import List

event_router = APIRouter(tags=["Events"])

events = []

@event_router.get("/",response_model=List[Event])
async def retrieve_all_events():
    return events

@event_router.get("/{id}",response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events: 
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event ID not exist!"
    )

@event_router.post("/new",status_code=status.HTTP_201_CREATED)
async def create_event(body: Event = Body(...)):
    events.append(body)
    return {"message" : "Event Created Successfully"}


@event_router.delete("/{id}")
async def delete_event(id: int):
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message":"Event Deleted Successfully" 
            }
    raise HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event Id not exist!"
    )

@event_router.delete("/")
async def delete_all_events():
    events.clear()
    return {
        "message": "Event deleted successfully"
    }