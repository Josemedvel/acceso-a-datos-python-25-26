from flask import Flask, request
import random

app = Flask(__name__)

# ruta con parámetro
@app.route('/user/<username>')
def show_user(username):
    return f"Hola {username}"

# ruta accesible desde GET y POST
@app.route('/aleatorio', methods=["POST", "GET"])
def random_number():
    return f"Tu número es {random.randint(0,100)}"

@app.route("/saludo/metodo", methods=["POST", "GET", "PUT", "DELETE"])
def saludo_metodo():
    response = "Hola desde "
    match request.method:
        case "POST":
            response += "POST"
        case "GET":
            response += "GET"
        case "PUT":
            response += "PUT"
        case "DELETE":
            response += "DELETE"
    return response

# simulamos que consultamos un usuario de una bd
@app.get('/usuarios/<id>')
def get_user(id):
    return {
        "nombre" : "Perico",
        "email" : "peri@gmail.com"
        }

@app.post('/usuarios')
def post_user():
    return f"Usuario creado con éxito!"



if __name__ == "__main__":
    app.run(debug=True)