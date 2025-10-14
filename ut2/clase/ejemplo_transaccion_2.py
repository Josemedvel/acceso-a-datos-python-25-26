import sqlite3

conn = sqlite3.connect("../formula.db", isolation_level=None)
cursor = conn.cursor()

cursor.execute("BEGIN DEFERRED")
try:
    cursor.execute("UPDATE escuderias SET titulos_constructor = 16 WHERE nombre='Ferrari'")
    q = cursor.execute("SELECT * FROM escuderias")
    for l in q.fetchall():
        print(l)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    conn.close()

