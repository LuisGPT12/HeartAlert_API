from fastapi import FastAPI
from routes.usuarios_route import usuarios_route
from routes.doctor_route import doctores_route
from routes.pacientes_doctor import pacientes_doctor_route
from routes.historial_route import historial_route
from routes.usuario_google_route import usuarioGoogle_route 
from routes.pacientes_route import paciente_route
from routes.alertas_route import alerta_router
from routes.electrocardiograma_router import electroCardiograma_route

app = FastAPI()

# Incluir el router de usuarios_route con la etiqueta 'Usuarios'
app.include_router(usuarios_route, tags=["usuarios"])
app.include_router(doctores_route, tags=["doctores"])
app.include_router(pacientes_doctor_route, tags=["pacientes_doctor"])
app.include_router(historial_route, tags=["historial"])
app.include_router(usuarioGoogle_route, tags=["usuariosGoogle"])
app.include_router(paciente_route, tags=["pacientes_doctor"])
app.include_router(alerta_router, tags=["alertas"])
app.include_router(electroCardiograma_route, tags=["alertas"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)  