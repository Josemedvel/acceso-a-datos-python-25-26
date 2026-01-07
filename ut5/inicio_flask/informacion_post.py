from flask import Flask, request

app = Flask(__name__)

@app.post("/alta-usuario")
def alta_usuario():
    return request.form

@app.delete("/baja-usuario")
def baja_usuario():
    id_user = request.form.get("id")
    if not id_user:
        return f"No se ha proporcionado un usuario", 400
    try:
        num_id = int(id_user)
    except ValueError as e:
        return "Tipo de dato no válido: El id debe ser un número entero positivo", 400
    if num_id <= 0:
        return f"Usuario no válido: El id del usuario debe ser un número entero positivo", 400
    return f"Usuario {num_id} eliminado correctamente", 200
    
        


if __name__ == "__main__":
    app.run(debug=True)