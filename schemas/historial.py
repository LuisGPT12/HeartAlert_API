from pydantic import BaseModel
from typing import Optional

class Historial(BaseModel):
    ID_Historial: Optional[int] = None
    COD_Paciente: int
    Tipo_sangre: str
    Alergias: Optional[str] = None
    diagnóstico: str
    Observaciones: Optional[str] = None

    class Config:
        from_attributes = True