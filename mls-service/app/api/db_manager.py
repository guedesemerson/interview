from app.api.models import MlsIn, MlsOut, MlsUpdate
from app.api.db import mls, database


async def add_mls(payload: MlsIn):
    query = mls.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_mls():
    query = mls.select()
    return await database.fetch_all(query=query)


async def get_mls(id):
    query = mls.select(mls.c.id==id)
    return await database.fetch_one(query=query)


async def delete_mls(id: int):
    query = mls.delete().where(mls.c.id==id)
    return await database.execute(query=query)


async def update_mls(id: int, payload: MlsIn):
    query = (
        mls
        .update()
        .where(mls.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)