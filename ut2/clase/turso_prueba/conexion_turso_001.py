import envyte
import libsql

db_url = envyte.get("DB_URL")
api_token = envyte.get("API_TOKEN")

conn = libsql.connect("pruebaaad")
cursor = conn.cursor()
#cursor.execute("""
#                CREATE TABLE IF NOT EXISTS profesores(
#                    dni INTEGER PRIMARY KEY,
#                    nombre TEXT NOT NULL,
#                    tutor TEXT NOT NULL DEFAULT "S"
#               )
#               """)
#cursor.execute("DELETE FROM alumnos WHERE nombre IN('Francisco', 'Menganito')")
#cursor.execute("INSERT INTO alumnos (nombre, ciclo) VALUES('Francisco', 'DAW')")

#conn.commit()
q = cursor.execute("SELECT * FROM alumnos").fetchall()
for i in q:
    print(i)