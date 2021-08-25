from app.api.models import PropertyIn, PropertyOut, PropertyUpdate
from app.api.db import properties, database


async def add_property(payload: PropertyIn):
    query = properties.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_property(id):
    query = properties.select(properties.c.id==id)
    return await database.fetch_one(query=query)