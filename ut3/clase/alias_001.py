from peewee import *
from datetime import datetime

db = SqliteDatabase(":memory:")

db.execute_sql("PRAGMA foreign_keys = ON;")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField(max_length=30)

class Tweet(BaseModel):
    post = CharField(max_length=248)
    user = ForeignKeyField(User, backref="tweets")

db.create_tables([User, Tweet], safe= True)

u1 = User.create(name="Jaimito")
u2 = User.create(name="Juanito")
u3 = User.create(name="Joselito")

Tweet.create(post="Trabajar 60 horas a la semana es lo mínimo admisible", user=u1)
Tweet.create(post="Haciendo pellas desde chiquito", user=u2)
Tweet.create(post="Suspendería a todos si pudiera", user=u3)

query = (
    User
    .select(User.name.alias("nombre completo"))
    .where(User.name.contains("ni"))
)
resultado = query.execute()

for r in resultado:
    print(r.alias("nombre completo"))