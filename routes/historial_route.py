from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, historial
from schemas.historial import Historial

historial_route = APIRouter(
    prefix="/api/heatalert/historial",
    tags=["historial"]
)

@historial_route.get("/", response_model=List[Historial])
def get_historiales():
    with engine.connect() as conn:
        result = conn.execute(historial.select()).fetchall()
        return [Historial(**dict(row._mapping)) for row in result]

@historial_route.get("/{historial_id}", response_model=Historial)
def get_historial(historial_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            historial.select().where(historial.c.ID_Historial == historial_id)
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Historial no encontrado")
        return Historial(**dict(result._mapping))

@historial_route.post("/", response_model=Historial, status_code=201)
def create_historial(hist: Historial):
    with engine.connect() as conn:
        insert_stmt = historial.insert().values(**hist.dict(exclude_unset=True))
        result = conn.execute(insert_stmt)
        conn.commit()
        new_id = result.inserted_primary_key[0]
        result = conn.execute(
            historial.select().where(historial.c.ID_Historial == new_id)
        ).first()
        return Historial(**dict(result._mapping))

@historial_route.put("/{historial_id}", response_model=Historial)
def update_historial(historial_id: int, hist: Historial):
    with engine.connect() as conn:
        update_stmt = historial.update().where(
            historial.c.ID_Historial == historial_id
        ).values(**hist.dict(exclude_unset=True))
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Historial no encontrado")
        conn.commit()
        result = conn.execute(
            historial.select().where(historial.c.ID_Historial == historial_id)
        ).first()
        return Historial(**dict(result._mapping))

@historial_route.delete("/{historial_id}", status_code=204)
def delete_historial(historial_id: int):
    with engine.connect() as conn:
        delete_stmt = historial.delete().where(historial.c.ID_Historial == historial_id)
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Historial no encontrado")
        conn.commit()
        return None