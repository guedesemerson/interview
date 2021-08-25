from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import MlsOut, MlsIn, MlsUpdate
from app.api import db_manager
from app.api.service import is_property_present

mls = APIRouter()


@mls.post('/', response_model=MlsIn, status_code=201)
async def create_mls(payload: MlsIn):
    for property_id in payload.property_id:
        if not is_property_present(property_id):
            raise HTTPException(status_code=404, detail=f"Property with given id:{property_id} not found")

    mls_id = await db_manager.add_mls(payload)
    response = {
        'id': mls_id,
        **payload.dict()
    }

    return response


@mls.get('/', response_model=List[MlsOut])
async def get_mls():
    return await db_manager.get_all_mls()


@mls.get('/{id}/', response_model=MlsOut)
async def get_mls(id: int):
    mls = await db_manager.get_mls(id)
    if not mls:
        raise HTTPException(status_code=404, detail="Mls not found")
    return mls


@mls.put('/{id}/', response_model=MlsOut)
async def update_mls(id: int, payload: MlsUpdate):
    mls = await db_manager.get_mls(id)
    if not mls:
        raise HTTPException(status_code=404, detail="Mls not found")

    update_data = payload.dict(exclude_unset=True)

    if 'property_id' in update_data:
        for property_id in payload.property_id:
            if not is_property_present(property_id):
                raise HTTPException(status_code=404, detail=f"Property with given id:{property_id} not found")

    mls_in_db = MlsIn(**mls)

    updated_mls = mls_in_db.copy(update=update_data)

    return await db_manager.update_mls(id, updated_mls)


@mls.delete('/{id}/', response_model=None)
async def delete_mls(id: int):
    mls = await db_manager.get_mls(id)
    if not mls:
        raise HTTPException(status_code=404, detail="Mls not found")
    return await db_manager.delete_mls(id)
