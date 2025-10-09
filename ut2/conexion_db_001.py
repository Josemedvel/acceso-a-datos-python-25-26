import sqlite3

with sqlite3.connect("base_de_datos.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS empleados")
    cursor.execute("DROP TABLE IF EXISTS clientes")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())


    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   salary REAL NOT NULL
                   )''')
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

    #cursor.execute("INSERT INTO empleados (name, salary) VALUES ('Juan', 20000), ('Maria', 25000)")
    conn.commit()
    
    
    cursor.execute("SELECT * FROM empleados")
    
    for r in cursor.fetchall():
        print(r)
