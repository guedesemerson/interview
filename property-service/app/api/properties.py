from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import PropertyOut, PropertyIn, PropertyUpdate
from app.api import db_manager

properties = APIRouter()


@properties.post('/', response_model=PropertyOut, status_code=201)
async def create_property(payload: PropertyIn):
    property_id = await db_manager.add_property(payload)

    response = {
        'id': property_id,
        **payload.dict()
    }

    return response


@properties.get('/{id}/', response_model=PropertyOut)
async def get_property(id: int):
    property = await db_manager.get_property(id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property