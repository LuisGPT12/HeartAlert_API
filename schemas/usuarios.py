from pydantic import BaseModel, condecimal
from datetime import datetime
from typing import Optional

class Usuarios(BaseModel):
    ID_Usuario: Optional[int]=None
    COD_Doctor: int=None
    nombre_usuario:str=None
    contrasenia:str= None

    class Config: 
        from_attributes = True 