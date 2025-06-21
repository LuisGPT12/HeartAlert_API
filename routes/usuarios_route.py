from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, usuarios
from schemas.usuarios import Usuarios

usuarios_route = APIRouter(
    prefix="/api/heatalert/usuarios",
    tags=["usuarios"]
)

# Obtener todos los usuarios
@usuarios_route.get("/", response_model=List[Usuarios])
def get_usuarios():
    with engine.connect() as conn:
        result = conn.execute(usuarios.select()).fetchall()
        return [Usuarios(**dict(row._mapping)) for row in result]

# Obtener usuario por ID
@usuarios_route.get("/{usuario_id}", response_model=Usuarios)
def get_usuario(usuario_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            usuarios.select().where(usuarios.c.ID_Usuario == usuario_id)
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return Usuarios(**dict(result._mapping))

# Crear usuario
@usuarios_route.post("/", response_model=Usuarios, status_code=201)
def create_usuario(usuario: Usuarios):
    with engine.connect() as conn:
        insert_stmt = usuarios.insert().values(**usuario.dict(exclude_unset=True))
        result = conn.execute(insert_stmt)
        conn.commit()
        new_id = result.inserted_primary_key[0]
        result = conn.execute(
            usuarios.select().where(usuarios.c.ID_Usuario == new_id)
        ).first()
        return Usuarios(**dict(result._mapping))

# Actualizar usuario
@usuarios_route.put("/{usuario_id}", response_model=Usuarios)
def update_usuario(usuario_id: int, usuario: Usuarios):
    with engine.connect() as conn:
        update_stmt = usuarios.update().where(
            usuarios.c.ID_Usuario == usuario_id
        ).values(**usuario.dict(exclude_unset=True))
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        conn.commit()
        result = conn.execute(
            usuarios.select().where(usuarios.c.ID_Usuario == usuario_id)
        ).first()
        return Usuarios(**dict(result._mapping))

# Eliminar usuario
@usuarios_route.delete("/{usuario_id}", status_code=204)
def delete_usuario(usuario_id: int):
    with engine.connect() as conn:
        delete_stmt = usuarios.delete().where(usuarios.c.ID_Usuario == usuario_id)
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        conn.commit()
        return None