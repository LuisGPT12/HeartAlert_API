from pydantic import BaseModel
from typing import Optional

class PacienteDoctor(BaseModel):
    COD_Paciente: int
    COD_Doctor: int

    class Config:
        from_attributes = True