from pydantic import BaseModel
from typing import Optional

class Video(BaseModel):
    id_video: Optional[int] = None
    descripcion: str

    class Config:
        from_attributes = True