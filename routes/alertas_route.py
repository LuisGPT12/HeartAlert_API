from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, alertas
from schemas.alertas import Alerta

alerta_router = APIRouter(
    prefix="/api/heatalert/alertas",
    tags=["alertas"]
)

@alerta_router.get("/", response_model=List[Alerta])
def get_alertas():
    with engine.connect() as conn:
        result = conn.execute(alertas.select()).fetchall()
        return [Alerta(**dict(row._mapping)) for row in result]

@alerta_router.get("/{paciente_id}", response_model=List[Alerta])
def get_alertas_by_paciente(paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            alertas.select().where(alertas.c.COD_Paciente == paciente_id)
        ).fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron alertas para este paciente")
        return [Alerta(**dict(row._mapping)) for row in result]

@alerta_router.post("/", response_model=Alerta, status_code=201)
def create_alerta(alerta: Alerta):
    with engine.connect() as conn:
        insert_stmt = alertas.insert().values(**alerta.dict(exclude_unset=True))
        result = conn.execute(insert_stmt)
        conn.commit()
        new_id = result.inserted_primary_key[0]
        result = conn.execute(
            alertas.select().where(alertas.c.ID_Alerta == new_id)
        ).first()
        return Alerta(**dict(result._mapping))

@alerta_router.put("/{alerta_id}", response_model=Alerta)
def update_alerta(alerta_id: int, alerta: Alerta):
    with engine.connect() as conn:
        update_stmt = alertas.update().where(
            alertas.c.ID_Alerta == alerta_id
        ).values(**alerta.dict(exclude_unset=True))
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Alerta no encontrada")
        conn.commit()
        result = conn.execute(
            alertas.select().where(alertas.c.ID_Alerta == alerta_id)
        ).first()
        return Alerta(**dict(result._mapping))

@alerta_router.delete("/{alerta_id}", status_code=204)
def delete_alerta(alerta_id: int):
    with engine.connect() as conn:
        delete_stmt = alertas.delete().where(alertas.c.ID_Alerta == alerta_id)
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Alerta no encontrada")
        conn.commit()
        return None