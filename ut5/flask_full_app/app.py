from conexion_pool import r
import sqlite3
from flask import Flask, redirect, url_for, request, g, jsonify
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "notes.db")
CACHE_KEY = "notes:list"
CACHE_TTL = 60


def get_db():
    if "db" not in g:
        conn = sqlite3.connect(DB_PATH)
        g.db = conn
        init_db(conn)
    return g.db


def init_db(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now'))
                 )                 
    """)
    conn.commit()


def query_notes():
    db = get_db()
    rows = db.execute("SELECT id, title, content, created_at FROM notes ORDER BY created_at DESC").fetchall()
    return rows


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db:
        db.close() # cerramos la conexión


@app.get("/notes")
def list_notes():
    cached = r.get(CACHE_KEY)
    if cached: # si hay algo, se devuelven
        import json
        notes = json.loads(cached)
        return {"source": "cache", "notes": notes}
    notes = query_notes()
    import json
    r.setex(CACHE_KEY, CACHE_TTL, json.dumps(notes))
    return jsonify({"source": "db", "notes": notes}), 200


@app.post("/notes")
def create_note():
    data = request.get_json(silent=True) or {}
    print(data)
    title = (data.get("title") or "").strip()
    content = (data.get("content") or "").strip()
    if not title or not content:
        return jsonify({"error": "title and content are required"}), 400

    db = get_db()
    cur = db.execute("INSERT INTO notes(title, content) VALUES(?,?)", (title, content))
    db.commit()
    note_id = cur.lastrowid

    r.delete(CACHE_KEY) # es importante invalidar la cache, si no, no nos enteramos de los cambios
    return jsonify({"id": note_id, "title": title, "content": content}), 201


@app.delete("/notes/<int:note_id>") #al poner el tipo, si la petición es incorrecta se envía un 404 automáticamente
def delete_note(note_id):
    db = get_db()
    cur = db.execute("DELETE FROM notes WHERE id=?", (note_id,))
    db.commit()
    if cur.rowcount == 0:
        return jsonify({"error": "Not found"}), 404
    r.delete(CACHE_KEY) # también invalidamos al borrar
    return "", 204


@app.post("/cache/clear")
def clear_cache():
    r.delete(CACHE_KEY)
    return redirect(url_for("list_notes"), code=303)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)