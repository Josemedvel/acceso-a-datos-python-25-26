import sqlite3
import json
from conexion_pool import r

DB_PATH = "persis_redis.db"

def update_user(user_id: int, name: str = None, age: int = None):
    """Actualiza usuario en BD y elimina caché"""
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        
        if name and age:
            cur.execute("UPDATE users SET name=?, age=? WHERE id=?", (name, age, user_id))
        elif name:
            cur.execute("UPDATE users SET name=? WHERE id=?", (name, user_id))
        elif age:
            cur.execute("UPDATE users SET age=? WHERE id=?", (age, user_id))
        
        # Invalidar caché (eliminar clave)
        r.delete(f"user:{user_id}")
        
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def delete_user(user_id: int):
    """Elimina usuario de BD y caché"""
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id=?", (user_id,))
        
        # Invalidar caché
        r.delete(f"user:{user_id}")
        
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
