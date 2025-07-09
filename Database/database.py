import os
from sqlalchemy import create_engine, MetaData, Table

# Configuración de la conexión a la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:12345@127.0.0.1:3306/heartalertdb")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)  # Cambiar a False en producción

# Metadata y tablas
metadata = MetaData()

usuarios = Table('usuarios', metadata, autoload_with=engine)
doctor = Table('doctor', metadata, autoload_with=engine)
pacientes_doctor = Table('pacientes_doctor', metadata, autoload_with=engine)
historial = Table('historial', metadata, autoload_with=engine)
usuariosGoogle=Table('usuario_google', metadata, autoload_with=engine)
pacientes=Table('pacientes', metadata, autoload_with=engine)
alertas = Table('alertas', metadata, autoload_with=engine)
electrocardiograma = Table('electrocardiograma', metadata, autoload_with=engine)