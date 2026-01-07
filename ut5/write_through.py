import sqlite3
from conexion_pool import r
from pprint import pp
import json


DB_PATH = "persis_redis.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
            """)
        conn.commit()

def create_user_write_through(name:str, age:int):
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        user_id = cur.lastrowid
        user = {"id": user_id, "name": name, "age": age}

        pipe = r.pipeline() # por defecto se hace transacción
        pipe.set(f"user:{user_id}", json.dumps(user))
        pipe.execute()

        conn.commit()
        return user
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_user(user_id:int):
    key = f"user:{user_id}"
    cached = r.get(key)
    if cached:
        return json.loads(cached)

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, age FROM users WHERE id=?", (user_id,))
        row = cur.fetchone()
    if not row:
        return None
    
    user = {"id": row[0], "name": row[1], "age": row[2]}
    r.setex(key, 100, json.dumps(user))
    return user


if __name__ == "__main__":
    init_db()
    u = create_user_write_through("Paco", 21)
    print("Usuario creado en SQLite y Redis")
    pp(u)
    print("Buscado en el caché:")
    pp(get_user(u["id"]))