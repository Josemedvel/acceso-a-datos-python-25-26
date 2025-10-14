import sqlite3

def subir_sueldo(salario, porcentaje):
    return salario * (1 + porcentaje / 100)


with sqlite3.connect("base_de_datos.db") as conn:
    conn.create_function("AUMENTO", 2, subir_sueldo)
    cursor = conn.cursor()
    cursor.execute("SELECT name, AUMENTO(salary, 10) FROM empleados")
    print(cursor.fetchone())

    # modificación de un empleado usando la función
    cursor.execute("""
    UPDATE empleados SET salary = AUMENTO(salary, 10) WHERE name = 'Juan';                   
""")
    q = cursor.execute("SELECT name, AUMENTO(salary, 10) FROM empleados")
    for e in q.fetchall():
        print(e)
