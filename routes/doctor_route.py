from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, doctor
from schemas.doctor import Doctor

doctores_route = APIRouter( 
    prefix="/api/heatalert/doctores",
    tags=["doctores"]
)

@doctores_route.get("/", response_model=List[Doctor])
def get_doctores():
    with engine.connect() as conn:
        result = conn.execute(doctor.select()).fetchall()
        return [Doctor(**dict(row._mapping)) for row in result]

@doctores_route.get("/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            doctor.select().where(doctor.c.ID_Doctor == doctor_id)
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")
        return Doctor(**dict(result._mapping))

@doctores_route.post("/", response_model=Doctor, status_code=201)
def create_doctor(doc: Doctor):
    with engine.connect() as conn:
        insert_stmt = doctor.insert().values(
            nombre_doctor=doc.nombre_doctor,
            apellido_doctor=doc.apellido_doctor,
            especialidad=doc.especialidad,
            Verificacion_ID=doc.Verificacion_ID
        )
        result = conn.execute(insert_stmt)
        conn.commit()
        new_id = result.inserted_primary_key[0]
        result = conn.execute(
            doctor.select().where(doctor.c.ID_Doctor == new_id)
        ).first()
        return Doctor(**dict(result._mapping))

@doctores_route.put("/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doc: Doctor):
    with engine.connect() as conn:
        update_stmt = doctor.update().where(
            doctor.c.ID_Doctor == doctor_id
        ).values(
            nombre_doctor=doc.nombre_doctor,
            apellido_doctor=doc.apellido_doctor,
            especialidad=doc.especialidad,
            Verificacion_ID=doc.Verificacion_ID
        )
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")
        conn.commit()
        result = conn.execute(
            doctor.select().where(doctor.c.ID_Doctor == doctor_id)
        ).first()
        return Doctor(**dict(result._mapping))

@doctores_route.delete("/{doctor_id}", status_code=204)
def delete_doctor(doctor_id: int):
    with engine.connect() as conn:
        delete_stmt = doctor.delete().where(doctor.c.ID_Doctor == doctor_id)
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")
        conn.commit()
        return None