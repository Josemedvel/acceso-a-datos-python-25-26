from conexion_pool import r
import json
from pprint import pp
import redis
import sqlite3

DB_PATH = "joyeria.db"
TTL = 20

def inicializar_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS relojes(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        marca TEXT NOT NULL,
                        modelo TEXT NOT NULL,
                        precio_venta DECIMAL NOT NULL,
                        num_serie TEXT NOT NULL
                    )
                    ''')
        cur.execute(
            '''
            INSERT INTO relojes (marca, modelo, precio_venta, num_serie) VALUES 
            ("rolex", "submariner", 17000, "27345728134"),
            ("CASIO", "fw91", 20.0, "245234623"),
            ("OMEGA", "pristine", 5000, "2340582075")
            '''
        )
    print("Ingesta terminada!")

def buscar_reloj(id):
    key = f"relojes:{id}"
    reloj = r.get(key)
    r.expire(key, TTL)
    
    if reloj: # está en caché
        print("reloj encontrado en caché")
        return json.loads(reloj)
    else:
        print("reloj no en caché")
        reloj = {}
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            resultado = cur.execute("SELECT marca, modelo, precio_venta, num_serie FROM relojes WHERE id=?", (id,))
            fila = resultado.fetchone()
            if fila:
                reloj["marca"] = fila[0]
                reloj["modelo"] = fila[1]
                reloj["precio_venta"] = fila[2]
                reloj["num_serie"] = fila[3]
                r.setex(key, TTL, json.dumps(reloj))
            else:
                raise Exception(f"Reloj con id [{id}] no existe en la db")
            return reloj

def actualizar_reloj(id, marca, modelo, precio_venta, num_serie):
    key = f"relojes:{id}"
    r.delete(key) # invalidación de caché
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE relojes SET marca=?, modelo=?, precio_venta=?, num_serie=?", (marca, modelo, precio_venta, num_serie))
        reloj_nuevo = {
            "marca": marca,
            "modelo": modelo,
            "precio_venta": precio_venta, 
            "num_serie": num_serie
        }
        r.setex(key, TTL, json.dumps(reloj_nuevo))
    
def main():
    #inicializar_db() # se ejecuta la primera vez solo
    pp(buscar_reloj(2))
    actualizar_reloj(
        id=2,
        marca="CASIO",
        modelo="G-SHOCK",
        precio_venta= 80,
        num_serie= "2435234623452"
    ) 
    

if __name__ == "__main__":
    main()
