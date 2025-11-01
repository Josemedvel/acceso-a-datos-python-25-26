from peewee import *
from datetime import datetime

db = SqliteDatabase("Jovellanos.db")
db.connect()

class Alumno(Model):
    nia = TextField(primary_key=True)
    nombre = TextField()
    fecha_nac = DateField()
    curso = IntegerField(constraints=[Check("curso IN (1,2)")])
    
    class Meta:
        database = db

#db.drop_tables([Alumno], safe=True)
db.create_tables([Alumno], safe=True)

#alumno = Alumno(nia="1234567", nombre="Jaimito", fecha_nac="2000-10-26", curso=4)
#alumno.save()

#alumno = Alumno.create(nia="1234567", nombre="Jaimito", fecha_nac="2000-10-26", curso=1)
#alumno = Alumno.create(nia="88283471", nombre="Pedrito", fecha_nac="1989-12-25", curso=2)
resultados = Alumno.select()
for r in resultados:
    print(r.nia)