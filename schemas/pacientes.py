from pydantic import BaseModel
from typing import Optional
from datetime import date

class Paciente(BaseModel):
    ID_Paciente: Optional[int] = None
    nombre_paciente: Optional[str] = None
    apellido_paciente: Optional[str] = None
    cedula_paciente: Optional[str] = None
    fecha_Nacimiento: Optional[date] = None
    sexo_paciente: str
    email: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    contacto_emergencia_nombre: Optional[str] = None
    contacto_emergencia_telefono: Optional[str] = None

    class Config:
        from_attributes = True