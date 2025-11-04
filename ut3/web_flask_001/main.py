from flask import Flask, request, render_template_string, redirect, url_for
from peewee import *

db = SqliteDatabase("usuarios.db")

class Usuario(Model):
    nombre = CharField(max_length=30)
    edad = IntegerField(constraints=[Check("edad > 0 & edad < 120")])
    class Meta:
        database = db


db.connect()
db.create_tables([Usuario], safe=True)

#Usuario.create(nombre = "Mariola", edad = 31)
#Usuario.create(nombre = "Pedro", edad = 25)

app = Flask(__name__)

@app.route("/") # Raíz de la web
def index():
    usuarios = Usuario.select()
    html =  """
            <h1>Lista de usuarios</h1>
            <ul>
            {% for user in usuarios %}
                <li>{{user.nombre}} - {{user.edad}} años</li>
            {% endfor %}
            </ul>
            <a href="/new"> Agregar usuario </a>
            """
    return render_template_string(html, usuarios=usuarios)


@app.route("/new", methods=["GET", "POST"])
def agregar_usuario():
    if request.method == "POST": # o sea, hemos enviado el formulario
        nombre = request.form["name"]
        edad = int(request.form["age"])
        Usuario.create(nombre=nombre, edad=edad)
        return redirect(url_for("index"))
    
    html = """
    <h1>Nuevo usuario</h1>
    <form method="POST">
        Nombre: <input type="text" name="name"><br>
        Edad: <input type="number" name="age"><br>
        <input type="submit" value="Agregar">
    </form>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)