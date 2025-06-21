from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, pacientes
from schemas.pacientes import Paciente

paciente_route = APIRouter(
    prefix="/api/heatalert/pacientes",
    tags=["pacientes"]
)

@paciente_route.get("/", response_model=List[Paciente])
def get_pacientes():
    with engine.connect() as conn:
        result = conn.execute(pacientes.select()).fetchall()
        return [Paciente(**dict(row._mapping)) for row in result]

@paciente_route.get("/{paciente_id}", response_model=Paciente)
def get_paciente(paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            pacientes.select().where(pacientes.c.ID_Paciente == paciente_id)
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return Paciente(**dict(result._mapping))

@paciente_route.post("/", response_model=Paciente, status_code=201)
def create_paciente(paciente: Paciente):
    with engine.connect() as conn:
        insert_stmt = pacientes.insert().values(**paciente.dict(exclude_unset=True))
        result = conn.execute(insert_stmt)
        conn.commit()
        new_id = result.inserted_primary_key[0]
        result = conn.execute(
            pacientes.select().where(pacientes.c.ID_Paciente == new_id)
        ).first()
        return Paciente(**dict(result._mapping))

@paciente_route.put("/{paciente_id}", response_model=Paciente)
def update_paciente(paciente_id: int, paciente: Paciente):
    with engine.connect() as conn:
        update_stmt = pacientes.update().where(
            pacientes.c.ID_Paciente == paciente_id
        ).values(**paciente.dict(exclude_unset=True))
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        conn.commit()
        result = conn.execute(
            pacientes.select().where(pacientes.c.ID_Paciente == paciente_id)
        ).first()
        return Paciente(**dict(result._mapping))

@paciente_route.delete("/{paciente_id}", status_code=204)
def delete_paciente(paciente_id: int):
    with engine.connect() as conn:
        delete_stmt = pacientes.delete().where(pacientes.c.ID_Paciente == paciente_id)
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        conn.commit()
        return None