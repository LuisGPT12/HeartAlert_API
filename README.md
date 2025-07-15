# HeartAlert API

API REST para el monitoreo y gestión de datos de electrocardiogramas y alertas cardíacas.

## 🚀 Características

- **Gestión de usuarios**: Registro y autenticación de usuarios y doctores
- **Monitoreo cardíaco**: Almacenamiento y análisis de lecturas de electrocardiograma
- **Sistema de alertas**: Notificaciones automáticas basadas en anomalías cardíacas
- **Historial médico**: Registro completo de pacientes y sus datos médicos
- **Integración con Google**: Autenticación con Google OAuth

## 📋 Requisitos

- Python 3.11+
- MySQL 8.0+
- FastAPI
- SQLAlchemy
- PyMySQL

## 🔧 Instalación

1. **Clonar el repositorio**
```bash
git clone <tu-repo>
cd HeartAlert_API
```

2. **Crear entorno virtual**
```bash
python -m venv fastapi_env
fastapi_env\Scripts\activate  # Windows
```

3. **Instalar dependencias**
```bash
pip install fastapi uvicorn sqlalchemy pymysql cryptography
```

4. **Configurar base de datos**
```sql
CREATE DATABASE heartalertdb;
```

5. **Configurar variables de entorno**
```bash
# Crear archivo .env
DATABASE_URL=mysql+pymysql://root:12345@127.0.0.1:3306/heartalertdb?auth_plugin=mysql_native_password
```

## 🚀 Uso

### Ejecutar el servidor
```bash
uvicorn main:app --host 0.0.0.0 --port 80
```

### Documentación API
- Swagger UI: `http://localhost:80/docs`
- ReDoc: `http://localhost:80/redoc`

## 📁 Estructura del Proyecto

```
HeartAlert_API/
├── main.py                 # Archivo principal de la aplicación
├── Database/
│   └── database.py        # Configuración de base de datos
├── routes/                # Endpoints de la API
│   ├── usuarios_route.py
│   ├── doctor_route.py
│   ├── alertas_route.py
│   └── electrocardiograma_router.py
├── schemas/               # Modelos Pydantic
│   ├── usuarios.py
│   ├── doctor.py
│   └── alertas.py
└── fastapi_env/          # Entorno virtual
```

## 🔗 Endpoints Principales

### Usuarios
- `GET /api/heatalert/usuarios/` - Obtener todos los usuarios
- `POST /api/heatalert/usuarios/` - Crear usuario
- `PUT /api/heatalert/usuarios/{id}` - Actualizar usuario

### Doctores
- `GET /api/heatalert/doctores/` - Obtener todos los doctores
- `POST /api/heatalert/doctores/` - Crear doctor

### Alertas
- `GET /api/heatalert/alertas/` - Obtener todas las alertas
- `GET /api/heatalert/alertas/paciente/{id}` - Alertas por paciente
- `POST /api/heatalert/alertas/` - Crear alerta

### Electrocardiograma
- `GET /api/heatalert/electrocardiograma/` - Obtener lecturas
- `POST /api/heatalert/electrocardiograma/` - Crear lectura

## 🗄️ Base de Datos

### Tablas principales:
- `usuarios` - Información de usuarios
- `doctor` - Información de doctores
- `pacientes` - Datos de pacientes
- `electrocardiograma` - Lecturas cardíacas
- `alertas` - Sistema de alertas
- `historial` - Historial médico

## 🔒 Autenticación

La API utiliza autenticación basada en tokens y Google OAuth para el acceso seguro.

## 🚨 Solución de Problemas

### Error de autenticación MySQL
```bash
pip install cryptography
# O agregar ?auth_plugin=mysql_native_password a la URL
```

### Error de puerto 80
```bash
# Usar puerto alternativo
uvicorn main:app --host 0.0.0.0 --port 8000
```

