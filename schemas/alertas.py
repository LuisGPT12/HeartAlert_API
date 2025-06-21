from pydantic import BaseModel
from typing import Optional

class Alerta(BaseModel):
    ID_Alerta: Optional[int] = None
    COD_Lectura: int
    COD_Paciente: int
    tipo_alerta: str
    atendido: str

    class Config:
        from_attributes = True