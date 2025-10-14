import sqlite3

def a_mayusculas(text):
    return text.upper()

def redondeo(num_campeonatos):
    return round(num_campeonatos, -1)


with sqlite3.connect("../formula.db") as conn:
    cursor = conn.cursor()
    conn.create_function("MAYUS", 1, a_mayusculas)
    conn.create_function("REDONDEO", 1, redondeo)
    q = cursor.execute("SELECT MAYUS('hola buenas tardes')")
    print(q.fetchone())

    cursor.execute("UPDATE escuderias SET titulos_constructor=REDONDEO(titulos_constructor) WHERE nombre = 'Red Bull Racing'")
    q2 = cursor.execute("SELECT * FROM escuderias")
    print(q2.fetchall())