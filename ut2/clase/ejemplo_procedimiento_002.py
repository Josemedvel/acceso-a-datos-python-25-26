import sqlite3

def actualizar_nombre_equipo(equipo, nombre=None):
    if nombre == None:
        nombre = input("Ingresa nuevo nombre")
    with sqlite3.connect("../formula.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE escuderias SET nombre=? WHERE nombre=?", (nombre, equipo))

def mostrar_equipos():
    with sqlite3.connect("../formula.db") as conn:
        cursor = conn.cursor()
        q = cursor.execute("SELECT * FROM escuderias")
        for l in q.fetchall():
            print(l)

actualizar_nombre_equipo("Racing Bulls")
mostrar_equipos()