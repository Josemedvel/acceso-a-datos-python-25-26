import sqlite3

with sqlite3.connect("base_de_datos.db") as conn:
    cursor = conn.cursor()
    #cursor.execute('''
#INSERT INTO empleados (name, salary) VALUES ('Pedro', 20000)
#                   ''')
    q = cursor.execute("SELECT * FROM empleados")
    for i in q.fetchall():
        print(i)