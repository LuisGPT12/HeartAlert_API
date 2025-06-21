from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Electrocardiograma(BaseModel):
    ID_Lectura: Optional[int] = None
    COD_Paciente: int
    tiempo_actual: datetime
    frecuencia_cardiaca: int
    balance_cardiaca_hrv: float

    class Config:
        from_attributes = True