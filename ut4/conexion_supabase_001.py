from peewee import *
import envyte


db = PostgresqlDatabase(
    host=envyte.get("HOST"),
    database=envyte.get("DATABASE"), # nombre de la BD
    port=envyte.get("PORT"),
    user=envyte.get("USER")
)
db.connect()