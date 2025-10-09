import sqlite3

with sqlite3.connect("chinook.sqlite") as conn:
    cursor = conn.cursor()

    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute("SELECT * FROM track")
    resultados = cursor.fetchall()
    for r in resultados:
        print(r)