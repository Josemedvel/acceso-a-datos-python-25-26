from datetime import datetime
from peewee import *

db = SqliteDatabase("prueba.db")

class Usuario(Model):
    nombre = TextField(primary_key=True)
    edad = IntegerField(constraints=[Check("edad >= 0")])
    class Meta:
        database = db

db.drop_tables([Usuario])
db.create_tables([Usuario], safe=True)

Usuario.create(nombre="Manuel", edad=20)

resultados = Usuario.select().execute()

for i in resultados:
    print(i.nombre)


