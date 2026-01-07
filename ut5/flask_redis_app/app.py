from conexion_pool import r
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TTL_SECONDS = 60 # van a ser los segundos de vida de la información
KEY = "clicks_counter" # la clave que vamos a usar para redis

def get_counter():
    val = r.get(KEY)
    count = int(val) if val else 0 # si no existe el valor la cuenta es 0
    ttl = r.ttl(KEY) # -2 si no existe, -1 si no tiene caducidad, >0 los segundos restantes
    ttl_remaining = ttl if ttl and ttl > 0 else 0
    return count, ttl_remaining

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #incrementamos el contador y reiniciamos tiempo de vida
        count = r.incr(KEY)
        r.expire(KEY, TTL_SECONDS)
        return redirect(url_for("index"))
    
    count, ttl_remaining = get_counter()
    return render_template("index.html", count = count, ttl=ttl_remaining, ttl_seconds=TTL_SECONDS)

@app.post("/reset")
def reset():
    r.delete(KEY)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
