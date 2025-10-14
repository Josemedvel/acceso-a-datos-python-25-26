import sqlite3

with sqlite3.connect("../formula.db") as conn:
    cursor = conn.cursor()
    cursor.execute("UPDATE escuderias SET titulos_constructor = 1 WHERE nombre='Ferrari'")
    cursor.execute("SELECT * FROM escuderias")
    for esc in cursor.fetchall():
        print(esc)