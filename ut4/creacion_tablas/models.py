from database import db
from peewee import *
from playhouse.postgres_ext import *
import datetime

class BaseModel(Model):
    class Meta:
        database = db

class Producto(BaseModel):
    nombre = CharField(max_length=50)
    especificaciones = JSONField() # Campo de texto JSON, menos eficiente como dijimos en las diapositivas
    opiniones = BinaryJSONField() # en este caso es binario, indexable
    precio = DecimalField()

