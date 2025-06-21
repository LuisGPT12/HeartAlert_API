from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, electrocardiograma
from schemas.electrocardiograma import Electrocardiograma

electroCardiograma_route = APIRouter(
    prefix="/api/heatalert/electrocardiograma",
    tags=["electrocardiograma"]
)
   
@electroCardiograma_route.get("/", response_model=List[Electrocardiograma])
def get_lecturas():
    with engine.connect() as conn:
        result = conn.execute(electrocardiograma.select()).fetchall()
        return [Electrocardiograma(**dict(row._mapping)) for row in result]

@electroCardiograma_route.get("/{lectura_id}", response_model=Electrocardiograma)
def get_lectura(lectura_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            electrocardiograma.select().where(electrocardiograma.c.ID_Lectura == lectura_id)
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Lectura no encontrada")
        return Electrocardiograma(**dict(result._mapping))

@electroCardiograma_route.post("/", response_model=Electrocardiograma, status_code=201)
def create_lectura(lectura: Electrocardiograma):
    with engine.connect() as conn:
        insert_stmt = electrocardiograma.insert().values(**lectura.dict(exclude_unset=True))
        result = conn.execute(insert_stmt)
        conn.commit()
        new_id = result.inserted_primary_key[0]
        result = conn.execute(
            electrocardiograma.select().where(electrocardiograma.c.ID_Lectura == new_id)
        ).first()
        return Electrocardiograma(**dict(result._mapping))

@electroCardiograma_route.put("/{lectura_id}", response_model=Electrocardiograma)
def update_lectura(lectura_id: int, lectura: Electrocardiograma):
    with engine.connect() as conn:
        update_stmt = electrocardiograma.update().where(
            electrocardiograma.c.ID_Lectura == lectura_id
        ).values(**lectura.dict(exclude_unset=True))
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Lectura no encontrada")
        conn.commit()
        result = conn.execute(
            electrocardiograma.select().where(electrocardiograma.c.ID_Lectura == lectura_id)
        ).first()
        return Electrocardiograma(**dict(result._mapping))

@electroCardiograma_route.delete("/{lectura_id}", status_code=204)
def delete_lectura(lectura_id: int):
    with engine.connect() as conn:
        delete_stmt = electrocardiograma.delete().where(electrocardiograma.c.ID_Lectura == lectura_id)
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Lectura no encontrada")
        conn.commit()
        return None