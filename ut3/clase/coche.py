from peewee import *
from datetime import datetime

db = SqliteDatabase("coches.db")

class BaseModel(Model):
    class Meta:
        database=db

class Coche(BaseModel):
    matricula = CharField(primary_key=True,max_length=7,constraints=[Check("LENGTH(matricula)=7")])
    fecha_fabricacion = DateField(default=datetime.now(), constraints=[Check(f"(julianday({datetime.now().date()}) - fecha_fabricacion) >= 0")])


db.create_tables([Coche], safe=True)

Coche.create(matricula="1235GMT", fecha_fabricacion="2025-11-22")

