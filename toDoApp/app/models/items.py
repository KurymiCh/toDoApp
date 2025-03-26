import uuid
import datetime
from typing import List, Optional
from pydantic import BaseModel

class ItemCreateRequest(BaseModel):
    title: str
    desc: str
    todo: datetime.datetime
    done: bool | None=False

class ItemUpdateRequest(BaseModel):
    title: Optional[str]
    desc: Optional[str]
    todo: Optional[datetime.datetime]
    done: Optional[bool] | None=False

class ItemResponse(BaseModel):
    id: uuid.UUID
    title: str
    desc: str
    todo: datetime.datetime
    done: bool
    created_at:datetime.datetime
    updated_at:datetime.datetime
    deleted_at:datetime.datetime | None

class ItemListResponse(BaseModel):
    items:List[ItemResponse]


