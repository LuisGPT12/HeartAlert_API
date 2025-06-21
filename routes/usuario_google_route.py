from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, usuariosGoogle
from schemas.usuario_google import UsuarioGoogle

usuarioGoogle_route = APIRouter(
    prefix="/api/heatalert/usuariosGoogle",
    tags=["usuariosGoogle"]
)

@usuarioGoogle_route.get("/", response_model=List[UsuarioGoogle])
def get_usuarios_google():
    with engine.connect() as conn:
        result = conn.execute(usuariosGoogle.select()).fetchall()
        return [UsuarioGoogle(**dict(row._mapping)) for row in result]

@usuarioGoogle_route.get("/{usuariosGoogle_id}", response_model=UsuarioGoogle)
def get_usuariosGoogle(usuariosGoogle_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            usuariosGoogle.select().where(usuariosGoogle.c.ID_UsuarioGoogle == usuariosGoogle_id)
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Usuario Google no encontrado")
        return UsuarioGoogle(**dict(result._mapping))

@usuarioGoogle_route.post("/", response_model=UsuarioGoogle, status_code=201)
def create_usuariosGoogle(usuario: UsuarioGoogle):
    with engine.connect() as conn:
        insert_stmt = usuariosGoogle.insert().values(**usuario.dict(exclude_unset=True))
        result = conn.execute(insert_stmt)
        conn.commit()
        new_id = result.inserted_primary_key[0]
        result = conn.execute(
            usuariosGoogle.select().where(usuariosGoogle.c.ID_UsuarioGoogle == new_id)
        ).first()
        return UsuarioGoogle(**dict(result._mapping))

@usuarioGoogle_route.put("/{usuariosGoogle_id}", response_model=UsuarioGoogle)
def update_usuariosGoogle(usuariosGoogle_id: int, usuario: UsuarioGoogle):
    with engine.connect() as conn:
        update_stmt = usuariosGoogle.update().where(
            usuariosGoogle.c.ID_UsuarioGoogle == usuariosGoogle_id
        ).values(**usuario.dict(exclude_unset=True))
        result = conn.execute(update_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuario Google no encontrado")
        conn.commit()
        result = conn.execute(
            usuariosGoogle.select().where(usuariosGoogle.c.ID_UsuarioGoogle == usuariosGoogle_id)
        ).first()
        return UsuarioGoogle(**dict(result._mapping))

@usuarioGoogle_route.delete("/{usuariosGoogle_id}", status_code=204)
def delete_usuariosGoogle(usuariosGoogle_id: int):
    with engine.connect() as conn:
        delete_stmt = usuariosGoogle.delete().where(usuariosGoogle.c.ID_UsuarioGoogle == usuariosGoogle_id)
        result = conn.execute(delete_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuario Google no encontrado")
        conn.commit()
        return None