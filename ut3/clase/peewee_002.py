from peewee import *
from datetime import datetime
import os
import sys

if len(sys.argv) != 2:
    print("Tienes que añadir el nombre de la base de datos")
    sys.exit(-1)

nombre_bd = sys.argv[1]

if os.path.exists(nombre_bd):
    print("Conectando a la base de datos...")
else:
    print("No se ha encontrado la base de datos, creándola...")

db = SqliteDatabase(nombre_bd)

class BaseModel(Model):
    class Meta:
        database=db

class Alumno(BaseModel):
    nia = TextField(primary_key=True)
    nombre = TextField()
    fecha_nac = DateField()
    curso = IntegerField(constraints=[Check("curso IN (1,2)")])

alumnos = Alumno.select()

for alumno in alumnos:
    print(alumno)