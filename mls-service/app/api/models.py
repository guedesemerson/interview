from pydantic import BaseModel
from typing import List, Optional


class MlsIn(BaseModel):
    source_id: str
    property_id: List[int]
    first_american_listing_id: str


class MlsOut(MlsIn):
    id: int


class MlsUpdate(MlsIn):
    source_id: Optional[str] = None
    property_id: Optional[List[int]] = None
    first_american_listing_id: Optional[str] = None
