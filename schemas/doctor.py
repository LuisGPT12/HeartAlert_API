from pydantic import BaseModel
from typing import Optional

class Doctor(BaseModel):
    ID_Doctor: Optional[int] = None
    nombre_doctor: str
    apellido_doctor: str
    especialidad: str
    Verificacion_ID: str

    class Config:
        from_attributes = True