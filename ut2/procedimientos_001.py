import sqlite3

def subir_sueldo(salario, porcentaje):
    return salario * (1 + porcentaje / 100)


with sqlite3.connect("base_de_datos.db") as conn:
    conn.create_function("AUMENTO", 2, subir_sueldo)
    cursor = conn.cursor()
    cursor.execute("SELECT AUMENTO(10000, 10)")
    print(cursor.fetchone())
