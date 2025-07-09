from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Electrocardiograma(BaseModel):
    ID_Lectura: Optional[int] = None
    COD_Paciente: int
    tiempo_actual: datetime
    frecuencia_cardiaca: float
    balance_cardiaca_hrv: Optional [float] = None
    class Config:
        from_attributes = True