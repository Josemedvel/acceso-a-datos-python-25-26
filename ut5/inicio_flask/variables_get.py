from flask import Flask, request

app = Flask(__name__)

@app.get("/preferencias")
def seleccion_tema():
    if request.args.get("tema"):
        color = "black"
        tema = request.args.get("tema")
        match tema:
            case "red":
                color = "red"
            case "blue":
                color = "blue"
            case "black":
                color = "black"
            case _:
                return "No se ha elegido un color válido", 400
        

        return f'''
            <html>
            <head>
                <style>
                    * {{
                        color: {color};
                    }}
                </style>
            </head>
            <body>
                <h1>Tema seleccionado: {tema}</h1>
                <p>El color aplicado es: {color}</p>
            </body>
            </html>
        '''
    else:
        return '''
            <html>
            <body>
                <h1>No se ha seleccionado ningún tema</h1>
                <p>Usa ?tema=red, ?tema=blue o cualquier otro valor</p>
            </body>
            </html>
        '''


if __name__ == "__main__":
    app.run(debug=True)