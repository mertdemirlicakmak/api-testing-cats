from pydantic import BaseModel, Field
from typing import Optional

class StatusModel(BaseModel):
    verified: Optional[bool]
    sentCount: Optional[int]

class FactModel(BaseModel):
    _id: str
    __v: int
    user: str
    text: str
    createdAt: str
    updatedAt: str
    deleted: bool
    used: Optional[bool] = None
    source: Optional[str] = None
    type: str
    status: StatusModel