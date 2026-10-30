from pydantic import BaseModel, Field
from typing import Optional

class Hotel(BaseModel):
    id: Optional[int] = None
    name: str
    location: str
    rating: float = Field(..., ge=1.0, le=5.0)
    rooms_available: int