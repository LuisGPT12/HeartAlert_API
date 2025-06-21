from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from Database.database import engine,  pacientes_doctor 
from schemas.pacientes_doctor import PacienteDoctor

pacientes_doctor_route = APIRouter(
    prefix="/api/heatalert/pacientes_doctor",
    tags=["pacientes_doctor"]
)

@pacientes_doctor_route.get("/", response_model=List[PacienteDoctor])
def get_asignaciones():
    with engine.connect() as conn:
        result = conn.execute(pacientes_doctor.select()).fetchall()
        return [PacienteDoctor(**dict(row._mapping)) for row in result]

@pacientes_doctor_route.get("/{cod_paciente}/{cod_doctor}", response_model=PacienteDoctor)
def get_asignacion(cod_paciente: int, cod_doctor: int):
    with engine.connect() as conn:
        result = conn.execute(
            pacientes_doctor.select().where(
                (pacientes_doctor.c.COD_Paciente == cod_paciente) &
                (pacientes_doctor.c.COD_Doctor == cod_doctor)
            )
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Asignación no encontrada")
        return PacienteDoctor(**dict(result._mapping))

@pacientes_doctor_route.post("/", response_model=PacienteDoctor, status_code=201)
def create_asignacion(asignacion: PacienteDoctor):
    with engine.connect() as conn:
        insert_stmt = pacientes_doctor.insert().values(**asignacion.dict(exclude_unset=True))
        conn.execute(insert_stmt)
        conn.commit()
        result = conn.execute(
            pacientes_doctor.select().where(
                (pacientes_doctor.c.COD_Paciente == asignacion.COD_Paciente) &
                (pacientes_doctor.c.COD_Doctor == asignacion.COD_Doctor)
            )
        ).first()
        return PacienteDoctor(**dict(result._mapping))

@pacientes_doctor_route.put("/{cod_paciente}/{cod_doctor}", response_model=PacienteDoctor)
def update_asignacion(cod_paciente: int, cod_doctor: int, asignacion: PacienteDoctor):
    with engine.connect() as conn:
        update_stmt = pacientes_doctor.update().where(
            (pacientes_doctor.c.COD_Paciente == cod_paciente) &
            (pacientes_doctor.c.COD_Doctor == cod_doctor)
        ).values(**asignacion.dict(exclude_unset=True))
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Asignación no encontrada")
        conn.commit()
        result = conn.execute(
            pacientes_doctor.select().where(
                (pacientes_doctor.c.COD_Paciente == cod_paciente) &
                (pacientes_doctor.c.COD_Doctor == cod_doctor)
            )
        ).first()
        return PacienteDoctor(**dict(result._mapping))

@pacientes_doctor_route.delete("/{cod_paciente}/{cod_doctor}", status_code=204)
def delete_asignacion(cod_paciente: int, cod_doctor: int):
    with engine.connect() as conn:
        delete_stmt = pacientes_doctor.delete().where(
            (pacientes_doctor.c.COD_Paciente == cod_paciente) &
            (pacientes_doctor.c.COD_Doctor == cod_doctor)
        )
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Asignación no encontrada")
        conn.commit()
        return None

@pacientes_doctor_route.get("/por_doctor/{cod_doctor}", response_model=List[Dict[str, Any]])
def get_pacientes_por_doctor(cod_doctor: int):
    with engine.connect() as conn:
        join_stmt = pacientes_doctor.join(
            tabla_pacientes, pacientes_doctor.c.COD_Paciente == tabla_pacientes.c.ID_Paciente
        )
        query = (
            pacientes_doctor.select()
            .select_from(join_stmt)
            .where(pacientes_doctor.c.COD_Doctor == cod_doctor)
        )
        result = conn.execute(query).fetchall()
        return [dict(row._mapping) for row in result]