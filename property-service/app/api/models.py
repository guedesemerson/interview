from pydantic import BaseModel
from typing import List, Optional


class PropertyIn(BaseModel):
    fips: str
    apn: str = None


class PropertyOut(PropertyIn):
    id: int


class PropertyUpdate(PropertyIn):
    fips: Optional[str] = None
    apn: Optional[str] = None