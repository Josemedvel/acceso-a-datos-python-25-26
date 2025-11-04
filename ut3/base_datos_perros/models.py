from database import db
from datetime import datetime
from peewee import *

class BaseModel(Model):
    """Modelo base para todos los modelos"""
    class Meta:
        database = db 

class PerroGuia(BaseModel):
    chip = AutoField()
    fecha_nac = DateField()
    sexo = CharField(max_length=1,constraints=[Check("sexo IN ('H', 'M')")])
    raza = TextField()
    nivel_entrenamiento = IntegerField(constraints=[Check("nivel_entrenamiento BETWEEN 1 AND 5")])
    institucion = TextField()
