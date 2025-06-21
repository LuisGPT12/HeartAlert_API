from pydantic import BaseModel
from typing import Optional

class UsuarioGoogle(BaseModel):
    ID_UsuarioGoogle: Optional[int] = None
    COD_Doctor: int
    email: Optional[str] = None

    class Config:
        from_attributes = True