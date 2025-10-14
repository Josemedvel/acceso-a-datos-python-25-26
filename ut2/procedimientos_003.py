import sqlite3

def aumentar_salario(nombre, porcentaje):
    with sqlite3.connect("base_de_datos.db") as conn:
        cur = conn.cursor()
        cur.execute("UPDATE empleados SET salary = salary * (1 + ?/100) WHERE name = ?", (porcentaje, nombre))
        conn.commit()


def imprimir_empleados():
    with sqlite3.connect("base_de_datos.db") as conn:
        cur = conn.cursor()
        q = cur.execute("SELECT * FROM empleados")
        for e in q.fetchall():
            print(e)

imprimir_empleados()
print()
aumentar_salario("Maria", 0.05)
imprimir_empleados()


